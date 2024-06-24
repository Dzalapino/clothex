from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from sqlmodel import SQLModel
from repository.item_controller import init_item_stocks, item_router, init_item_defs
# from repository.order_controller import order_router
from repository.db_connection import delete_db, engine
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

origins = ['http://localhost:4200', 'http://localhost']

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    if form_data.username == "admin" and form_data.password == "admin":
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": form_data.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

# @app.get("/admin")
# async def read_protected_route(current_user: str = Depends(get_current_user)):
#     return {"message": f"Hello admin {current_user}"}

async def get_access_token(username: str, password: str) -> str:
    url = "http://localhost:8000/api/token"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data={"username": username, "password": password})
        if response.status_code == 200:
            token_data = response.json()
            return token_data["access_token"]
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to get access token")
        
async def fetch_item_list(access_token: str) -> dict:
    url = "http://localhost:8000/api/products/my"
    headers = {"Authorization": f"Bearer {access_token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch items")

async def fetch_item_details(id: int, access_token: str):
    url = "http://localhost:8000/api/products/" + str(id) + "/items"
    headers = {"Authorization": f"Bearer {access_token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch item details")

@app.get("/data")
async def get_data():
    access_token = await get_access_token('230359@edu.p.lodz.pl', 'Outdoor')
    items = await fetch_item_list(access_token)
    list = []
    for item in items:
        details = await fetch_item_details(item['product_id'], access_token)
        list.append(details)
    return list

@app.get("/data/{id}")
async def get_data_by_id(id: int):
    access_token = await get_access_token('230359@edu.p.lodz.pl', 'Outdoor')
    details = await fetch_item_details(id, access_token)
    return details


app.include_router(item_router)

if __name__ == "__main__":
    delete_db()
    init_item_defs()
    init_item_stocks()
    from uvicorn import run
    run(app, host='0.0.0.0', port=8001)