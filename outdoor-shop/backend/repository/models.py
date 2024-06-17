from sqlmodel import SQLModel, Field

class ItemDef(SQLModel, table=True):
    id: int = Field(default = None, primary_key = True)
    name: str
    color: str

class ItemStock(SQLModel, table=True):
    id: int = Field(default = None, primary_key = True)
    productId: int
    quantity: int