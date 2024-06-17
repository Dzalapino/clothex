from sqlmodel import SQLModel, Field


class LocalProduct(SQLModel, table=True, tablename="local_products"):
    id: int = Field(default=None, primary_key=True, nullable=False)
    amount_in_stock: int = Field(default=0, nullable=False)
