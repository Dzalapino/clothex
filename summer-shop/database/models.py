"""
SQLModel models for the database tables
"""
from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal
from typing import Optional


class HQProduct(SQLModel, table=True, tablename="hq_products"):
    __tablename__ = "hq_products"
    id: int = Field(default=None, primary_key=True, nullable=False)
    category: str = Field(nullable=False)
    name: str = Field(nullable=False)
    image_url: Optional[str] = Field(default="", nullable=True)
    description: Optional[str] = Field(default="", nullable=True)
    price_pln: Decimal = Field(default=0, max_digits=7, decimal_places=2, nullable=False)

    local_product: Optional["LocalProduct"] = Relationship(back_populates="hq_product")


class LocalProduct(SQLModel, table=True, tablename="local_products"):
    __tablename__ = "local_products"
    id: int = Field(default=None, primary_key=True, nullable=False)
    hq_product_id: int = Field(nullable=False, foreign_key="hq_products.id")
    amount_in_stock: int = Field(default=0, nullable=False)

    hq_product: Optional[HQProduct] = Relationship(back_populates="local_product")


class User(SQLModel, table=True, tablename="users"):
    __tablename__ = "users"
    id: int = Field(default=None, primary_key=True, nullable=False)
    email: str = Field(nullable=False, unique=True)
    password_hashed: str = Field(nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    role: str = Field(default="user", nullable=False)
