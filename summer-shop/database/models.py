"""
SQLModel models for the database tables
"""
from sqlmodel import SQLModel, Field


class LocalProduct(SQLModel, table=True, tablename="local_products"):
    id: int = Field(default=None, primary_key=True, nullable=False)
    amount_in_stock: int = Field(default=0, nullable=False)


class User(SQLModel, table=True, tablename="users"):
    id: int = Field(default=None, primary_key=True, nullable=False)
    email: str = Field(nullable=False, unique=True)
    password_hashed: str = Field(nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    role: str = Field(default="user", nullable=False)
