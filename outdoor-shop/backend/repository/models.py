from sqlmodel import SQLModel, Field
from typing import List

class ItemStock(SQLModel, table=True):
    id: int = Field(default = None, primary_key = True)
    productId: int
    quantity: int