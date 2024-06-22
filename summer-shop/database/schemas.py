"""
Pydantic schemas for the database models to parse the request body
"""
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, Field


class LocalProduct(BaseModel):
    id: Optional[int] = Field(null=False)
    hq_product_id: int = Field(null=False)
    amount_in_stock: int = Field(default=0, null=False)


class HQLocalJoined(BaseModel):
    id: int = Field(default=None, primary_key=True, nullable=False)
    hq_product_id: int = Field(null=False)
    category: str = Field(nullable=False)
    name: str = Field(nullable=False)
    image_url: Optional[str] = Field(default="", nullable=True)
    description: Optional[str] = Field(default="", nullable=True)
    price_pln: Decimal = Field(default=0, max_digits=7, decimal_places=2, nullable=False)
    amount_in_stock: int = Field(default=0, null=False)


class UserCreate(BaseModel):
    email: str = Field(null=False)
    password: str = Field(null=False)
    role: str = Field(default="user")


class UserLogin(BaseModel):
    email: str = Field(null=False)
    password: str = Field(null=False)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str
    role: str = "user"
