import pydantic as _pydantic
 
from typing import List

class _UserBase(_pydantic.BaseModel):
    email: str
 

"""
class UserCreate(_UserBase):
    hashed_password: str
 
    class Config:
        from_attributes = True
"""

class User(_UserBase):
    id: int
    shop_name: str
    email: str
    phone_number: str
    address: str
    grant_license: str
    hashed_password: str

    class Config:
        from_attributes = True

class Product(_pydantic.BaseModel):
    product_id: int
    product_category_id: int
    brand_id: int
    product_name: str
    # product category name !
    # product brand name !
    product_description: str

    class Config:
        from_attributes = True

class ProductsList(_pydantic.RootModel):
    root: List[Product]

# model of single product item data
class ProductItem(_pydantic.BaseModel):
    product_id: int
    product_name: str
    product_item_id: int
    product_code: str
    retail_price: float
    colour_id: int
    colour_name: str
    size_option_id: int
    size_option_name: str
    variation_id: int
    quantity_in_stock: int

    class Config:
        from_attributes = True

# model of product items list
class ProductsItemsList(_pydantic.RootModel):
    root: List[ProductItem]
    class Config:
        from_attributes = True