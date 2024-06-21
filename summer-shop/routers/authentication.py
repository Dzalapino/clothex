"""
This module contains the authentication endpoints for the FastAPI application
"""
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from jose import JWTError, jwt
from sqlmodel import select
from passlib.context import CryptContext
from datetime import datetime, timedelta
import os
from typing import Optional

from database.models import User as UserModel
from database.schemas import UserCreate, Token, TokenData
from database.db_connection import get_session

authentication_router = APIRouter(prefix="/auth")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Environment Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "6yIVmXB8hVs9Wm8JBRfUuH7AbGn9Jafm1tNPRf7LfYA")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Token Blacklist
token_blacklist = set()


# Helper functions
def get_user_by_email(email: str) -> Optional[UserModel]:
    with get_session() as session:
        statement = select(UserModel).where(UserModel.email == email)
        return session.exec(statement).first()


def create_user(user: UserCreate) -> UserModel:
    with get_session() as session:
        hashed_password = pwd_context.hash(user.password)  # Hash the plain password
        db_user = UserModel(
            email=user.email,
            password_hashed=hashed_password,
            role=user.role
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)) -> UserModel:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        role: str = payload.get("role")
        if email is None or role is None:
            raise credentials_exception
        token_data = TokenData(email=email, role=role)
    except JWTError:
        raise credentials_exception

    # Check if the token is blacklisted
    if token in token_blacklist:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has been invalidated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = get_user_by_email(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


# Endpoints
@authentication_router.get("/me", response_model=TokenData)
def me(current_user: UserModel = Depends(get_current_user)):
    return JSONResponse(content={"email": current_user.email, "role": current_user.role})


@authentication_router.post("/register", response_model=Token)
def register(user: UserCreate):
    if get_user_by_email(user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    new_user = create_user(user)
    access_token = create_access_token(data={"sub": new_user.email, "role": new_user.role})
    return JSONResponse(content={"access_token": access_token, "token_type": "bearer"})


@authentication_router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = get_user_by_email(form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.password_hashed):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": db_user.email, "role": db_user.role})
    return JSONResponse(content={"access_token": access_token, "token_type": "bearer"})


@authentication_router.get("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    token_blacklist.add(token)
    return JSONResponse(content={"message": "Logout successful"})
