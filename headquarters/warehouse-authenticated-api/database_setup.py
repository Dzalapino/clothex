import products_database as _products_database, vendors_database as _vendors_database
import models as _models
import os
import passlib.hash as _hash

def create_products_database():
    return _products_database.Base.metadata.create_all(bind=_products_database.engine)

def create_vendors_database():
    return _vendors_database.Base.metadata.create_all(bind=_vendors_database.engine)

path = "./products_database.db"
try:
    os.remove(path)
    print("NEW DB SET UP")
except OSError as error:
    print(error)
    print("OLD DB NOT FOUND...")

path = "./vendors_database.db"
try:
    os.remove(path)
    print("NEW DB SET UP")
except OSError as error:
    print(error)
    print("OLD DB NOT FOUND...")

create_products_database()

def insert_vendors():
    from sqlalchemy import insert
    session = _vendors_database.SessionLocal()
    session.execute(
        insert(_models.User),
        [
            {"shop_name": "Summer LTD", "email": "224407@edu.p.lodz.pl", "phone_number": "1234567", "address": "X Y Z", "hashed_password": '$2b$12$Nac0ocdVdH.3ifiWshhYq.eIDpm/QLin/B6B3VSFhlyTxI05Q9LqC', "grant_license": "S"},
            {"shop_name": "Outdoor LTD", "email": "230359@edu.p.lodz.pl", "phone_number": "5234567", "address": "Z Y X", "hashed_password": '$2b$12$fI91gNRMr/Xuag3LxOwJH.8honUsQsT65KPyDaLnD7gntuvClJALW', "grant_license": "O"},
            {"shop_name": "Everything LTD", "email": "253234@edu.p.lodz.pl", "phone_number": "1212121", "address": "Y Z X", "hashed_password": '$2b$12$2V/P0I44jpZWpp6qnBaBaeVku7f0EEr54mLn6Z34cpJfTCREJFpWa', "grant_license": "OS"},
        ],
    )
    session.commit()

create_vendors_database()
insert_vendors()

def insert_colors():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Colour),
        [
            {"colour_name": "Red"},
            {"colour_name": "Black"},
            {"colour_name": "White"},
            {"colour_name": "Another"},
        ],
    )
    session.commit()

def insert_attribute_types():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Attribute_Type),
        [
            {"attribute_type_name": "Sale/New Season"},
            {"attribute_type_name": "Body Fit"},
        ],
    )
    session.commit()

def insert_attribute_options():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Attribute_Option),
        [
            {"attribute_type_id": 1, "attribute_option_name": "New Season"},
            {"attribute_type_id": 1, "attribute_option_name": "Sale"},
            {"attribute_type_id": 1, "attribute_option_name": "Regular Fit"},
            {"attribute_type_id": 1, "attribute_option_name": "Slim Fit"},
        ],
    )
    session.commit()

def insert_brands():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Brand),
        [
            {"brand_name": "sadidas", "brand_description": "It is nice brand"},
            {"brand_name": "jack&kcaj", "brand_description": "This brand is nice"},
            {"brand_name": "brandex", "brand_description": "Nice brand this is"},
            {"brand_name": "euro2024", "brand_description": "Brand this nice is"},
        ],
    )
    session.commit()

def insert_size_categories():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Size_Category),
        [
            {"size-category_name": "Clothing"},
            {"size-category_name": "Shoes"},
        ],
    )
    session.commit()


def insert_size_options():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Size_Option),
        [
            {"size_option_name": "M", "size_category_id": 1},
            {"size_option_name": "L", "size_category_id": 1},
            {"size_option_name": "XL", "size_category_id": 1},
            {"size_option_name": "39", "size_category_id": 2},
            {"size_option_name": "40", "size_category_id": 2},
            {"size_option_name": "41", "size_category_id": 2},
            {"size_option_name": "42", "size_category_id": 2},
            {"size_option_name": "43", "size_category_id": 2},
        ],
    )
    session.commit()

def insert_product_categories():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Product_Category),
        [
            {"category_name": "tshirts", "size_category_id": 1},
            {"category_name": "jackets", "size_category_id": 1},
            {"category_name": "shirts", "size_category_id": 1},
            {"category_name": "pants", "size_category_id": 1},
            {"category_name": "shoes", "size_category_id": 2},
        ],
    )
    session.commit()

def insert_products():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Product),
        [
            {"product_category_id": 1, "brand_id": 1,"product_name": "TS1","product_description": "classic tshirt","grant_license": "OS"},
            {"product_category_id": 1, "brand_id": 3,"product_name": "TS2","product_description": "slim-fit tshirt","grant_license": "OS"},
            {"product_category_id": 2, "brand_id": 2,"product_name": "J1","product_description": "stylish jacket","grant_license": "O"},
            {"product_category_id": 3, "brand_id": 3,"product_name": "S1","product_description": "hawaii party is yours because of this shirt","grant_license": "S"},
            {"product_category_id": 3, "brand_id": 4,"product_name": "S2","product_description": "slim-fit outdoor tactical shirt","grant_license": "O"},
            {"product_category_id": 4, "brand_id": 4,"product_name": "P4","product_description": "HQ cotton pants","grant_license": "O"},
            {"product_category_id": 5, "brand_id": 1,"product_name": "SH1","product_description": "breathable shoes made of wool in Zakopane","grant_license": "S"},
            {"product_category_id": 5, "brand_id": 2,"product_name": "SH2","product_description": "tactical shoes","grant_license": "O"},
        ],
    )
    session.commit()

def insert_products_items():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Product_Item),
        [
            {"retail_price": 69.9, "product_code": "TS1_C1", "colour_id": 1, "product_id": 1},
            {"retail_price": 69.9, "product_code": "TS1_C2", "colour_id": 2, "product_id": 1},
            {"retail_price": 89.9, "product_code": "TS2_C1", "colour_id": 3, "product_id": 2},
            {"retail_price": 489.9, "product_code": "J1_C1", "colour_id": 4, "product_id": 3},
            {"retail_price": 189.9, "product_code": "S1_C1", "colour_id": 4, "product_id": 4},
            {"retail_price": 159.9, "product_code": "S2_C1", "colour_id": 2, "product_id": 5},
            {"retail_price": 149.9, "product_code": "P1_C1", "colour_id": 3, "product_id": 6},
            {"retail_price": 219.9, "product_code": "P1_C2", "colour_id": 2, "product_id": 6},
            {"retail_price": 219.9, "product_code": "SH1_C1", "colour_id": 4, "product_id": 7},
            {"retail_price": 349.9, "product_code": "SH2_C2", "colour_id": 4, "product_id": 8},
        ],
    )
    session.commit()


def insert_products_images():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Product_Image),
        [
            {"product_item_id": 1, "image_url": "1xxx.xxx.xxx"},
            {"product_item_id": 1, "image_url": "1xxx.xxx.xxx"},
            {"product_item_id": 1, "image_url": "1xxx.xxx.xxx"},
            {"product_item_id": 1, "image_url": "1xxx.xxx.xxx"},

            {"product_item_id": 2, "image_url": "2xxx.xxx.xxx"},
            {"product_item_id": 2, "image_url": "2xxx.xxx.xxx"},
            {"product_item_id": 2, "image_url": "2xxx.xxx.xxx"},
            {"product_item_id": 2, "image_url": "2xxx.xxx.xxx"},

            {"product_item_id": 3, "image_url": "3xxx.xxx.xxx"},
            {"product_item_id": 3, "image_url": "3xxx.xxx.xxx"},
            {"product_item_id": 3, "image_url": "3xxx.xxx.xxx"},
            {"product_item_id": 3, "image_url": "3xxx.xxx.xxx"},

            {"product_item_id": 4, "image_url": "4xxx.xxx.xxx"},
            {"product_item_id": 4, "image_url": "4xxx.xxx.xxx"},
            {"product_item_id": 4, "image_url": "4xxx.xxx.xxx"},
            {"product_item_id": 4, "image_url": "4xxx.xxx.xxx"},

            {"product_item_id": 5, "image_url": "5xxx.xxx.xxx"},
            {"product_item_id": 5, "image_url": "5xxx.xxx.xxx"},
            {"product_item_id": 5, "image_url": "5xxx.xxx.xxx"},
            {"product_item_id": 5, "image_url": "5xxx.xxx.xxx"},

            {"product_item_id": 6, "image_url": "6xxx.xxx.xxx"},
            {"product_item_id": 6, "image_url": "6xxx.xxx.xxx"},
            {"product_item_id": 6, "image_url": "6xxx.xxx.xxx"},
            {"product_item_id": 6, "image_url": "6xxx.xxx.xxx"},

            {"product_item_id": 7, "image_url": "7xxx.xxx.xxx"},
            {"product_item_id": 7, "image_url": "7xxx.xxx.xxx"},
            {"product_item_id": 7, "image_url": "7xxx.xxx.xxx"},
            {"product_item_id": 7, "image_url": "7xxx.xxx.xxx"},

            {"product_item_id": 8, "image_url": "8xxx.xxx.xxx"},
            {"product_item_id": 8, "image_url": "8xxx.xxx.xxx"},
            {"product_item_id": 8, "image_url": "8xxx.xxx.xxx"},
            {"product_item_id": 8, "image_url": "8xxx.xxx.xxx"},

            {"product_item_id": 9, "image_url": "9xxx.xxx.xxx"},
            {"product_item_id": 9, "image_url": "9xxx.xxx.xxx"},
            {"product_item_id": 9, "image_url": "9xxx.xxx.xxx"},
            {"product_item_id": 9, "image_url": "9xxx.xxx.xxx"},

            {"product_item_id": 10, "image_url": "10xxx.xxx.xxx"},
            {"product_item_id": 10, "image_url": "10xxx.xxx.xxx"},
            {"product_item_id": 10, "image_url": "10xxx.xxx.xxx"},
            {"product_item_id": 10, "image_url": "10xxx.xxx.xxx"},

        ],
    )
    session.commit()

def insert_products_variations():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Product_Variation),
        [
            {"product_item_id": 1, "size_option_id": 1, "quantity_in_stock" : 29},
            {"product_item_id": 1, "size_option_id": 2, "quantity_in_stock" : 30},
            {"product_item_id": 1, "size_option_id": 3, "quantity_in_stock" : 41},

            {"product_item_id": 2, "size_option_id": 1, "quantity_in_stock" : 3},
            {"product_item_id": 2, "size_option_id": 2, "quantity_in_stock" : 12},
            {"product_item_id": 2, "size_option_id": 3, "quantity_in_stock" : 15},

            {"product_item_id": 3, "size_option_id": 1, "quantity_in_stock" : 11},
            {"product_item_id": 3, "size_option_id": 2, "quantity_in_stock" : 23},
            {"product_item_id": 3, "size_option_id": 3, "quantity_in_stock" : 31},

            {"product_item_id": 4, "size_option_id": 1, "quantity_in_stock" : 11},
            {"product_item_id": 4, "size_option_id": 2, "quantity_in_stock" : 65},
            {"product_item_id": 4, "size_option_id": 3, "quantity_in_stock" : 5},

            {"product_item_id": 5, "size_option_id": 1, "quantity_in_stock" : 123},
            {"product_item_id": 5, "size_option_id": 2, "quantity_in_stock" : 32},
            {"product_item_id": 5, "size_option_id": 3, "quantity_in_stock" : 213},

            {"product_item_id": 6, "size_option_id": 1, "quantity_in_stock" : 221},
            {"product_item_id": 6, "size_option_id": 2, "quantity_in_stock" : 232},
            {"product_item_id": 6, "size_option_id": 3, "quantity_in_stock" : 123},

            {"product_item_id": 7, "size_option_id": 1, "quantity_in_stock" : 23},
            {"product_item_id": 7, "size_option_id": 2, "quantity_in_stock" : 64},
            {"product_item_id": 7, "size_option_id": 3, "quantity_in_stock" : 75},

            {"product_item_id": 8, "size_option_id": 1, "quantity_in_stock" : 75},
            {"product_item_id": 8, "size_option_id": 2, "quantity_in_stock" : 46},
            {"product_item_id": 8, "size_option_id": 3, "quantity_in_stock" : 33},

            {"product_item_id": 9, "size_option_id": 4, "quantity_in_stock" : 1},
            {"product_item_id": 9, "size_option_id": 5, "quantity_in_stock" : 45},
            {"product_item_id": 9, "size_option_id": 6, "quantity_in_stock" : 65},
            {"product_item_id": 9, "size_option_id": 7, "quantity_in_stock" : 34},
            {"product_item_id": 9, "size_option_id": 8, "quantity_in_stock" : 0},

            {"product_item_id": 10, "size_option_id": 4, "quantity_in_stock" : 43},
            {"product_item_id": 10, "size_option_id": 5, "quantity_in_stock" : 42},
            {"product_item_id": 10, "size_option_id": 6, "quantity_in_stock" : 33},
            {"product_item_id": 10, "size_option_id": 7, "quantity_in_stock" : 52},
            {"product_item_id": 10, "size_option_id": 8, "quantity_in_stock" : 64},       
        ],
    )
    session.commit()

def insert_products_attributes():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.Product_Attribute),
        [
            {"product_id": 1, "attribute_option_id": 1},
            {"product_id": 1, "attribute_option_id": 3},
            {"product_id": 2, "attribute_option_id": 2},
            {"product_id": 2, "attribute_option_id": 4},
            {"product_id": 3, "attribute_option_id": 2},
            {"product_id": 3, "attribute_option_id": 3},
            {"product_id": 4, "attribute_option_id": 1},
            {"product_id": 4, "attribute_option_id": 3},
            {"product_id": 5, "attribute_option_id": 1},
            {"product_id": 5, "attribute_option_id": 4},
            {"product_id": 6, "attribute_option_id": 1},
            {"product_id": 7, "attribute_option_id": 1},
            {"product_id": 8, "attribute_option_id": 1},
        ],
    )
    session.commit()
"""

def insert_size_options():
    from sqlalchemy import insert
    session = _products_database.SessionLocal()
    session.execute(
        insert(_models.XXXXX),
        [
            {"size_option_name": "", "size_category_id": ""},
            {"size_option_name": "", "size_category_id": ""},
            {"size_option_name": "", "size_category_id": ""},
            {"size_option_name": "", "size_category_id": ""},
        ],
    )
    session.commit()
"""
insert_colors()
insert_attribute_types()
insert_attribute_options()
insert_brands()
insert_size_categories()
insert_size_options()
insert_product_categories()
insert_products()
insert_products_items()
insert_products_images()
insert_products_variations()
insert_products_attributes()