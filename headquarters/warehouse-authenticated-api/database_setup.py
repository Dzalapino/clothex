import products_database as _products_database, vendors_database as _vendors_database
import models as _models
import os
import datetime as _datetime
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

def insert_orders():
    from sqlalchemy import insert
    session = _vendors_database.SessionLocal()
    session.execute(
        insert(_models.Order),
        [
            {"order_time": _datetime.datetime.now() + _datetime.timedelta(days=-2), "order_confirmed": False, "order_send": False, "order_tracking_number": int((_datetime.datetime.now() + _datetime.timedelta(days=-2)).strftime('%Y%m%d')), "user_id": 1
            , "product_id": 1, "product_name" : "TS1", "product_item_id" : 1, "product_code" : "TS1_C1", "colour_id" : 1, "colour_name" : "Red", "size_option_id" : 1, "size_option_name" : "M", "order_quantity": 20},
            {"order_time": _datetime.datetime.now() + _datetime.timedelta(days=-1), "order_confirmed": False, "order_send": False, "order_tracking_number": int((_datetime.datetime.now() + _datetime.timedelta(days=-1)).strftime('%Y%m%d')), "user_id": 1
            , "product_id": 4, "product_name" : "S1", "product_item_id" : 5, "product_code" : "S1_C1", "colour_id" : 4, "colour_name" : "Another", "size_option_id" : 3, "size_option_name" : "XL", "order_quantity": 50},
            {"order_time": _datetime.datetime.now() + _datetime.timedelta(days=-0), "order_confirmed": False, "order_send": False, "order_tracking_number": int((_datetime.datetime.now() + _datetime.timedelta(days=-0)).strftime('%Y%m%d')), "user_id": 2
            , "product_id": 8, "product_name" : "SH2", "product_item_id" : 10, "product_code" : "SH2_C2", "colour_id" : 4, "colour_name" : "Another", "size_option_id" : 8, "size_option_name" : "43", "order_quantity": 30},
        ],
    )
    session.commit()


create_vendors_database()
insert_vendors()
insert_orders()

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
            {"product_item_id": 1, "image_url": "https://img01.ztat.net/article/spp-media-p1/8339e8dc60964d35a7b8558b04861a23/5a2b4a78a872453f8cbe13b4d71efa1c.jpg?imwidth=1800"},
            {"product_item_id": 1, "image_url": "https://img01.ztat.net/article/spp-media-p1/4f383d0922904d029b3ea92150c36e7c/2e7c8dc91de640cd9ae4e27284f12492.jpg?imwidth=1800"},
            {"product_item_id": 1, "image_url": "https://img01.ztat.net/article/spp-media-p1/3bf4d9b6ef8946b3877653c407ec8b1d/1a9c725e43f8410e80f4cb40b41ce864.jpg?imwidth=1800"},
            {"product_item_id": 1, "image_url": "https://img01.ztat.net/article/spp-media-p1/ab5b9c9a553248b2869ae853a447a69d/ca78723e5f4647b6b56e2d963cfef595.jpg?imwidth=1800"},

            {"product_item_id": 2, "image_url": "https://img01.ztat.net/article/spp-media-p1/0348f2dc66b24f3db961082680609072/6fba5221d8a1439f8c4c0f7ee4a8e796.jpg?imwidth=1800"},
            {"product_item_id": 2, "image_url": "https://img01.ztat.net/article/spp-media-p1/69745b6e8a394a409443c1eb13417fcf/20a67f3688eb4839bc40d321beefda7b.jpg?imwidth=1800"},
            {"product_item_id": 2, "image_url": "https://img01.ztat.net/article/spp-media-p1/dc8a41c4788e410c9181d46ca75bfcec/e7143ff08358468a81eaa2a15f163604.jpg?imwidth=1800"},
            {"product_item_id": 2, "image_url": "https://img01.ztat.net/article/spp-media-p1/7a5e472bf4404c3897b78dc53cb5fa21/81b8482a4c484421a88cd9563920e5c1.jpg?imwidth=1800"},

            {"product_item_id": 3, "image_url": "https://img01.ztat.net/article/spp-media-p1/241993c430f944df8869971ec3cd078d/6628195b444749a1a4e45eed437a6624.jpg?imwidth=1800"},
            {"product_item_id": 3, "image_url": "https://img01.ztat.net/article/spp-media-p1/e40e4c0e80e347cc9b326e75059ce2b4/4fa664c5eba4479aae5af4616ba57f0c.jpg?imwidth=1800"},
            {"product_item_id": 3, "image_url": "https://img01.ztat.net/article/spp-media-p1/4a9d6d3e9a0d4779936558485051ec6d/0b2d332aa6ac45af8ff3b70c62d3eca0.jpg?imwidth=1800"},
            {"product_item_id": 3, "image_url": "https://img01.ztat.net/article/spp-media-p1/abdf46b9ab1a44ceaadfef00fa65cd58/d8f61e29cb794908bd04d822e2e92d61.jpg?imwidth=1800"},

            {"product_item_id": 4, "image_url": "https://img01.ztat.net/article/spp-media-p1/9f3ffe2a32194db992499ec7175b4851/97dd9bc440904ae0820a4c1857d2e1d4.jpg?imwidth=1800"},
            {"product_item_id": 4, "image_url": "https://img01.ztat.net/article/spp-media-p1/315e5854abd542768eefbaccf6fda707/d6f3934facfd44829dcd728ec862488d.jpg?imwidth=1800"},
            {"product_item_id": 4, "image_url": "https://img01.ztat.net/article/spp-media-p1/e94b6cffd8974514bc376f45216b9975/b29203e1a76f4450864675a1202373a4.jpg?imwidth=1800"},
            {"product_item_id": 4, "image_url": "https://img01.ztat.net/article/spp-media-p1/1dedfa70f25a40a8a0374626ffb9628e/853e7772cc0447b8834c32d4e25afdd3.jpg?imwidth=1800"},

            {"product_item_id": 5, "image_url": "https://img01.ztat.net/article/spp-media-p1/a4c2fe9c924831cea2d129dc880b783e/0c01960ff69f45158930bcbcc64f3681.jpg?imwidth=1800"},
            {"product_item_id": 5, "image_url": "https://img01.ztat.net/article/spp-media-p1/47dd26f964f332cfbac96dff704e821f/c172361c48d74aa58d20bc6be87d7301.jpg?imwidth=1800"},
            {"product_item_id": 5, "image_url": "https://img01.ztat.net/article/spp-media-p1/37f27d869bb138959a92d89bba00fe99/a8ccfb1570584aceab6617e85bfb4b70.jpg?imwidth=1800"},
            {"product_item_id": 5, "image_url": "https://img01.ztat.net/article/spp-media-p1/b3122886e6dc387e96aa2b3a89d0871e/b1871bceda49406abcef2e381926bdfe.jpg?imwidth=1800"},

            {"product_item_id": 6, "image_url": "https://img01.ztat.net/article/spp-media-p1/f81b88a5cc744a4b9184686b7d209f5b/71ffbe8d54cd48238144f1d7cc6b7e8a.jpg?imwidth=1800"},
            {"product_item_id": 6, "image_url": "https://img01.ztat.net/article/spp-media-p1/85e74b8f99fb49b7942b82020cd1ec19/7f79694fc4974927bbce6445f8f6a421.jpg?imwidth=1800"},
            {"product_item_id": 6, "image_url": "https://img01.ztat.net/article/spp-media-p1/d3fcfab0f74343d8877f5d82de2a4b18/5c2a22089bf243f4a4a83fc6d762edb1.jpg?imwidth=1800"},
            {"product_item_id": 6, "image_url": "https://img01.ztat.net/article/spp-media-p1/f81eeb2fd5b7429ead9194f2af5f69bb/d487cafee16e4f449b7b06d55596ede9.jpg?imwidth=1800"},

            {"product_item_id": 7, "image_url": "https://img01.ztat.net/article/spp-media-p1/4a7852cf4b464a759f3f177fc5e99edc/6105eff5d990438e952dc86295ee5ed9.jpg?imwidth=1800"},
            {"product_item_id": 7, "image_url": "https://img01.ztat.net/article/spp-media-p1/3cb67905124c4e698a1460cf8a9c9257/4360799c68644a03bc4c2389c4cdfec3.jpg?imwidth=1800"},
            {"product_item_id": 7, "image_url": "https://img01.ztat.net/article/spp-media-p1/184be8b25ef64d7daed031e8068c632b/cdea122e4369464895e75aac0b5fce96.jpg?imwidth=1800"},
            {"product_item_id": 7, "image_url": "https://img01.ztat.net/article/spp-media-p1/4c2da142ed2d4581a0be1b4f0a625ba2/3cf52d317633494dbb7311c94c82232b.jpg?imwidth=1800"},

            {"product_item_id": 8, "image_url": "https://img01.ztat.net/outfit/be9800600ef34790a3707e41f3421aca/e993b79e3af0463a8bd56b8eb4d17079.jpg?imwidth=1800"},
            {"product_item_id": 8, "image_url": "https://img01.ztat.net/article/spp-media-p1/49dfc3f69fe74e1da1568676e8dc59c0/985b14f71bff454caed9f9ef39b56e10.jpg?imwidth=1800"},
            {"product_item_id": 8, "image_url": "https://img01.ztat.net/article/spp-media-p1/a3dd1fc2df104bccaed83ca03e91702b/ca96bcf69ba643c8959bd1dc2ccaa9b8.jpg?imwidth=1800"},
            {"product_item_id": 8, "image_url": "https://img01.ztat.net/article/spp-media-p1/d69507d70c4f49d19682d97955d97df4/e8c2512cdd964d7d89c1ebbc7f2543c6.jpg?imwidth=1800"},

            {"product_item_id": 9, "image_url": "https://img01.ztat.net/article/spp-media-p1/9fe23bf7b7b44efc8422ef72a79fa97b/2d3dd9c300934830a91cc95264823dd8.jpg?imwidth=1800&filter=packshot"},
            {"product_item_id": 9, "image_url": "https://img01.ztat.net/article/spp-media-p1/7f9541333cdc44318543ccf3894b35ae/3d37b4decd8a430b91b05a2b4df21ea6.jpg?imwidth=1800"},
            {"product_item_id": 9, "image_url": "https://img01.ztat.net/article/spp-media-p1/36a61fff46c34c9e9bf19e62e2da7e22/f3f3e107fa9743e297b443fdd9271062.jpg?imwidth=1800"},
            {"product_item_id": 9, "image_url": "https://img01.ztat.net/article/spp-media-p1/289d0c25bf47461f9b3231c573e4e02d/c586e21710824a1aa93f39e469a205d2.jpg?imwidth=1800"},

            {"product_item_id": 10, "image_url": "https://img01.ztat.net/article/spp-media-p1/a132ed80e5ab453cb208d9c1413025c3/4386c907ebfd40c99ab4ebff5052d470.jpg?imwidth=1800&filter=packshot"},
            {"product_item_id": 10, "image_url": "https://img01.ztat.net/article/spp-media-p1/7ff11f87a9644932ac68dde693d9de52/c510c16a72044b928debf8745c28e468.jpg?imwidth=1800"},
            {"product_item_id": 10, "image_url": "https://img01.ztat.net/article/spp-media-p1/580fcea3042f4b0fa1227d9b440f841c/053836fe4e1f407eb70677e753f2179c.jpg?imwidth=1800"},
            {"product_item_id": 10, "image_url": "https://img01.ztat.net/article/spp-media-p1/e09c1e3580d9483fb4176d022c916be4/d52197e251134c6c9ba36c3d95eddaec.jpg?imwidth=1800"},

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