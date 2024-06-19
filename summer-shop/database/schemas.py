# Pydantic schemas for the database models to parse the request body

from typing import Optional
from pydantic import BaseModel, Field


class LocalProduct(BaseModel):
    id: Optional[int] = Field(null=False)
    amount_in_stock: int = Field(default=0, null=False)
