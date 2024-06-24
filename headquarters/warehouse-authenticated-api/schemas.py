import pydantic as _pydantic
import datetime as _datetime
 
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
    user_id: int
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
    # product category name ! todo
    # product brand name ! todo
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

class ProductImage(_pydantic.BaseModel):
    image_id: int
    product_item_id: int
    image_url: str

    class Config:
        from_attributes = True

class ProductItemImagesList(_pydantic.RootModel):
    root: List[ProductImage]
    class Config:
        from_attributes = True

class ProductOrder(_pydantic.BaseModel):
    product_id: int
    product_name: str
    product_item_id: int
    product_code: str
    #retail_price: float
    colour_id: int
    colour_name: str
    size_option_id: int
    size_option_name: str
    variation_id: int
    quantity_in_stock: int
    order_quantity: int = 0
    order_tracking_number: int = 0

    class Config:
        from_attributes = True

class EmailSchema(_pydantic.BaseModel):
    email: List[_pydantic.EmailStr]
    
class EmailContent(_pydantic.BaseModel):
    recipent: str
    message: str
    subject: str

class BrandDetails(_pydantic.BaseModel):
    brand_id: int
    brand_name: str
    brand_description: str

    class Config:
        from_attributes = True