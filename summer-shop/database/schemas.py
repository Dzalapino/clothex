# Pydantic schemas for the database models to parse the request body

from typing import Optional
from pydantic import BaseModel, Field


class LocalProduct(BaseModel):
    id: Optional[int] = Field(null=False)
    amount_in_stock: int = Field(default=0, null=False)


class UserCreate(BaseModel):
    username: str = Field(null=False)
    email: str = Field(null=False)
    password: str = Field(null=False)


class UserLogin(BaseModel):
    username: str = Field(null=False)
    password: str = Field(null=False)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
