from sqlmodel import SQLModel, Field
from typing import List

class ItemDef(SQLModel, table=True):
    id: int = Field(default = None, primary_key = True)
    name: str
    color: str
    imgUrl: str

class ItemStock(SQLModel, table=True):
    id: int = Field(default = None, primary_key = True)
    productId: int
    quantity: int

# class Order(SQLModel, table=True):
#     id: int = Field(default = None, primary_key = True)
#     items: List[ItemStock]