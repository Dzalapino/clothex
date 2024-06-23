import datetime as _dt
from typing import List

import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash

import vendors_database as _vendors_database
import products_database as _products_database

class User(_vendors_database.Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    shop_name = _sql.Column(_sql.String, unique=True)
    email = _sql.Column(_sql.String, unique=True, index=True)
    phone_number = _sql.Column(_sql.String)
    address = _sql.Column(_sql.String)
    hashed_password = _sql.Column(_sql.String)
    grant_license = _sql.Column(_sql.String)
 
    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)



class Product_Category(_products_database.Base):
    __tablename__ = "product_category_table"
    product_category_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)

    product: _orm.Mapped[List["Product"]] = _orm.relationship(back_populates="product_category")

    size_category_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("size_category_table.size_category_id"))
    size_category: _orm.Mapped["Size_Category"] = _orm.relationship(back_populates="product_category")

    category_name = _sql.Column(_sql.String, unique=True)

class Product(_products_database.Base):
    __tablename__ = "product_table"
    product_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)

    product_category_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("product_category_table.product_category_id"))
    product_category: _orm.Mapped["Product_Category"] = _orm.relationship(back_populates="product")

    product_item: _orm.Mapped[List["Product_Item"]] = _orm.relationship(back_populates="product")

    brand_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("brand_table.brand_id"))
    brand: _orm.Mapped["Brand"] = _orm.relationship(back_populates="product")

    product_attribute: _orm.Mapped[List["Product_Attribute"]] = _orm.relationship(back_populates="product")

    product_name = _sql.Column(_sql.String, unique=True)
    product_description = _sql.Column(_sql.String, unique=False)
    grant_license = _sql.Column(_sql.String, unique=False)

    def __reprt__(self):
        return f"{self.__class__.__name__}, name: {self.product_name}, id: {self.product_id}"

class Product_Item(_products_database.Base):
    __tablename__ = "product_item_table"
    product_item_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)

    retail_price = _sql.Column(_sql.Float, unique=False)
    product_code = _sql.Column(_sql.String, unique=True)

    product_image: _orm.Mapped[List["Product_Image"]] = _orm.relationship(back_populates="product_item")

    colour_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("colour_table.colour_id"))
    colour: _orm.Mapped["Colour"] = _orm.relationship(back_populates="product_item")

    product_variation: _orm.Mapped[List["Product_Variation"]] = _orm.relationship(back_populates="product_item")


    product_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("product_table.product_id"))
    product: _orm.Mapped["Product"] = _orm.relationship(back_populates="product_item")

    def __reprt__(self):
        return f"{self.__class__.__name__}, code: {self.product_code}, id: {self.product_item_id}"


class Product_Image(_products_database.Base):
    __tablename__ = "product_image_table"
    image_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)
    
    product_item_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("product_item_table.product_item_id"))
    product_item: _orm.Mapped["Product_Item"] = _orm.relationship(back_populates="product_image")
    
    image_url = _sql.Column(_sql.String, unique=False)

class Colour(_products_database.Base):
    __tablename__ = "colour_table"
    colour_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)
    
    product_item: _orm.Mapped[List["Product_Item"]] = _orm.relationship(back_populates="colour")

    colour_name = _sql.Column(_sql.String, unique=True)

class Brand(_products_database.Base):
    __tablename__ = "brand_table"
    brand_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)
    
    product: _orm.Mapped[List["Product"]] = _orm.relationship(back_populates="brand")

    brand_name = _sql.Column(_sql.String, unique=True)
    brand_description = _sql.Column(_sql.String, unique=False)

class Product_Variation(_products_database.Base):
    __tablename__ = "product_variation_table"
    variation_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)
    
    product_item_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("product_item_table.product_item_id"))
    product_item: _orm.Mapped["Product_Item"] = _orm.relationship(back_populates="product_variation")
    
    size_option_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("size_option_table.size_option_id"))
    size_option: _orm.Mapped["Size_Option"] = _orm.relationship(back_populates="product_variation")


    quantity_in_stock = _sql.Column(_sql.Integer, unique=False)

class Size_Category(_products_database.Base):
    __tablename__ = "size_category_table"
    size_category_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)
    
    product_category: _orm.Mapped[List["Product_Category"]] = _orm.relationship(back_populates="size_category")
    
    size_option: _orm.Mapped[List["Size_Option"]] = _orm.relationship(back_populates="size_category")


    size_category_name = _sql.Column(_sql.String, unique=True)

class Size_Option(_products_database.Base):
    __tablename__ = "size_option_table"
    size_option_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)
    
    product_variation: _orm.Mapped[List["Product_Variation"]] = _orm.relationship(back_populates="size_option")

    size_category_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("size_category_table.size_category_id"))
    size_category: _orm.Mapped["Size_Category"] = _orm.relationship(back_populates="size_option")


    size_option_name = _sql.Column(_sql.String, unique=True)

class Product_Attribute(_products_database.Base):
    __tablename__ = "product_attribute_table"
    product_attribute_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)

    product_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("product_table.product_id"))
    product: _orm.Mapped["Product"] = _orm.relationship(back_populates="product_attribute")

    attribute_option_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("attribute_option_table.attribute_option_id"))
    attribute_option: _orm.Mapped["Attribute_Option"] = _orm.relationship(back_populates="product_attribute")


class Attribute_Option(_products_database.Base):
    __tablename__ = "attribute_option_table"
    attribute_option_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)

    product_attribute: _orm.Mapped[List["Product_Attribute"]] = _orm.relationship(back_populates="attribute_option")

    attribute_type_id: _orm.Mapped[int] = _orm.mapped_column(_sql.ForeignKey("attribute_type_table.attribute_type_id"))
    attribute_type: _orm.Mapped["Attribute_Type"] = _orm.relationship(back_populates="attribute_option")


    attribute_option_name = _sql.Column(_sql.String, unique=True)

class Attribute_Type(_products_database.Base):
    __tablename__ = "attribute_type_table"
    attribute_type_id: _orm.Mapped[int] = _orm.mapped_column(primary_key=True)

    attribute_option: _orm.Mapped[List["Attribute_Option"]] = _orm.relationship(back_populates="attribute_type")

    attribute_type_name = _sql.Column(_sql.String, unique=True)

