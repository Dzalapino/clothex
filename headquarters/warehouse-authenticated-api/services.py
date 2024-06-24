#fastapi-jwt/services.py
import fastapi as _fastapi
import fastapi.security as _security
import fastapi_mail as _fastapi_mail
import starlette.responses as _starlette_responses
import jwt as _jwt #pip install python_jwt https://pypi.org/project/python-jwt/
import datetime as _dt
import sqlalchemy.orm as _orm
import sqlalchemy as _sql
import passlib.hash as _hash
from dotenv import dotenv_values #pip install https://pypi.org/project/python_dotenv/

import datetime as _datetime

import vendors_database as _vendors_database, products_database as _products_database, models as _models, schemas as _schemas
 
config = dotenv_values(".env")
JWT_SECRET = config['JWT_SECRET']
ALGORITHM = config['ALGORITHM']
ACCESS_TOKEN_EXPIRE_MINUTES = int(config['ACCESS_TOKEN_EXPIRE_MINUTES'])

mailing_credentials = dotenv_values("mailing.env")
mailing_config = _fastapi_mail.ConnectionConfig(
    MAIL_USERNAME = mailing_credentials['EMAIL'],
    MAIL_PASSWORD = mailing_credentials['PASS'],
    MAIL_FROM = mailing_credentials['EMAIL'],
    MAIL_PORT = int(mailing_credentials['MAIL_PORT']),
    MAIL_SERVER = mailing_credentials['MAIL_SERVER'],
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

oauth2schema = _security.OAuth2PasswordBearer(tokenUrl="/api/token")

def get_db():
    db = _vendors_database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.email == email).first()
"""
async def create_user(user: _schemas.UserCreate, db: _orm.Session):
    user_obj = _models.User(
        email=user.email, hashed_password=_hash.bcrypt.hash(user.hashed_password)
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj
"""
async def authenticate_user(email: str, password: str, db: _orm.Session):
    user = await get_user_by_email(db=db, email=email)
    print(user)
 
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user
 
 
async def create_access_token(user: _models.User, expires_delta: _datetime.timedelta or None = None):
    user_obj = _schemas.User.from_orm(user).dict()

    if expires_delta:
        expire = _datetime.datetime.utcnow() + expires_delta
    else:
        expire = _datetime.datetime.utcnow() + _datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    user_obj.update({"exp": expire})

    token = _jwt.encode(user_obj, JWT_SECRET, algorithm=ALGORITHM)
 
    return dict(access_token=token, token_type="bearer")
 
async def get_current_user(
    db: _orm.Session = _fastapi.Depends(get_db),
    token: str = _fastapi.Depends(oauth2schema),
):
    try:
        payload = _jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        user = db.query(_models.User).get(payload["user_id"])
    except:
        raise _fastapi.HTTPException(
            status_code=401, detail="Invalid Email or Password"
        )
    return _schemas.User.from_orm(user)

def get_user_license(db, token):
    try:
        payload = _jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        user_grant_license = db.query(_models.User).get(payload["user_id"]).grant_license
        return user_grant_license
    except:
        raise _fastapi.HTTPException(
            status_code=401, detail="Invalid credentials or token expired"
        )
    
async def get_user_products(
    db: _orm.Session = _fastapi.Depends(get_db),
    token: str = _fastapi.Depends(oauth2schema),
):
    user_grant_license = get_user_license(db, token)
    tbl = _models.Product
    with _orm.Session(_products_database.engine) as session:
        statement = _sql.select(_models.Product).filter(tbl.grant_license.like('%'+user_grant_license+'%'))
        products_list = session.scalars(statement).all()
        p_list = [_schemas.Product.from_orm(row) for row in products_list]
        return p_list

async def get_selected_product_items(
    selected_product_id: int,
    db: _orm.Session = _fastapi.Depends(get_db),
    token: str = _fastapi.Depends(oauth2schema),
):
    user_grant_license = get_user_license(db, token)
    with _orm.Session(_products_database.engine) as session:
        products_list = session.query(
        _models.Product.product_id, _models.Product.product_name,
        _models.Product_Item.product_item_id, _models.Product_Item.product_code, _models.Product_Item.retail_price,
        _models.Colour.colour_id, _models.Colour.colour_name,
        _models.Size_Option.size_option_id, _models.Size_Option.size_option_name,
        _models.Product_Variation.variation_id, _models.Product_Variation.quantity_in_stock
        ).filter(
            _models.Product.grant_license.like('%'+user_grant_license+'%')
        ).filter(
            _models.Product.product_id==selected_product_id
        ).filter(
            _models.Product_Item.product_id==_models.Product.product_id
        ).filter(
            _models.Colour.colour_id==_models.Product_Item.colour_id
        ).filter(
            _models.Product_Variation.product_item_id==_models.Product_Item.product_item_id
        ).filter(
            _models.Size_Option.size_option_id==_models.Product_Variation.size_option_id
        ).filter(
            _models.Product_Category.product_category_id==_models.Product.product_category_id
        ).all()
        p_list = [_schemas.ProductItem.from_orm(row) for row in products_list]
        return p_list


async def send_email(email):
    html = f"""
    <h5>CSITatFTIMS LTD - Headquarter</h5>
    <br>
    <p>{email.message}</p>
    <br>
    <h6>Best Redards</p>
    <h6>CSITatFTIMS LTD - Headquarter</h6>
    """
    message = _fastapi_mail.MessageSchema(
    subject=email.subject,
    recipients=[email.recipent],
    body=html,
    subtype=_fastapi_mail.MessageType.html)
    fm = _fastapi_mail.FastMail(mailing_config)
    await fm.send_message(message)

def get_user_id(db, token):
    try:
        payload = _jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        user_id = db.query(_models.User).get(payload["user_id"]).user_id
        return user_id
    except:
        raise _fastapi.HTTPException(
            status_code=401, detail="Invalid credentials or token expired"
        )

async def register_order(user_id, order):
    order_object = _models.Order(
        order_time = _datetime.datetime.now(),
        order_confirmed = False,
        order_send = False,
        order_tracking_number = order.order_tracking_number,

        user_id = user_id,

        product_id = order.product_id,
        product_name = order.product_name,
        product_item_id = order.product_item_id,
        product_code = order.product_code,
        colour_id = order.colour_id,
        colour_name = order.colour_name,
        size_option_id = order.size_option_id,
        size_option_name = order.size_option_name,
        order_quantity = order.order_quantity,
    )

    with _orm.Session(_vendors_database.engine) as session:
        session.add(order_object)
        session.commit()
        session.refresh(order_object)

async def make_item_order(
    selected_product_id: int,
    selected_size_id: int,
    selected_colour_id,
    selected_quantity: int,
    db: _orm.Session = _fastapi.Depends(get_db),
    token: str = _fastapi.Depends(oauth2schema),
):
    user_grant_license = get_user_license(db, token)
    with _orm.Session(_products_database.engine) as session:
        item_data = session.query(
        _models.Product.product_id, _models.Product.product_name,
        _models.Product_Item.product_item_id, _models.Product_Item.product_code,
        _models.Colour.colour_id, _models.Colour.colour_name,
        _models.Size_Option.size_option_id, _models.Size_Option.size_option_name,
        _models.Product_Variation.variation_id, _models.Product_Variation.quantity_in_stock
        ).filter(
            _models.Product.grant_license.like('%'+user_grant_license+'%')
        ).filter(
            _models.Product.product_id==selected_product_id
        ).filter(
            _models.Colour.colour_id==selected_colour_id
        ).filter(
            _models.Size_Option.size_option_id==selected_size_id
        ).filter(
            _models.Product_Item.product_id==_models.Product.product_id
        ).filter(
            _models.Colour.colour_id==_models.Product_Item.colour_id
        ).filter(
            _models.Product_Variation.product_item_id==_models.Product_Item.product_item_id
        ).filter(
            _models.Size_Option.size_option_id==_models.Product_Variation.size_option_id
        ).filter(
            _models.Product_Category.product_category_id==_models.Product.product_category_id
        ).all()
        try:
            order = _schemas.ProductOrder.from_orm(item_data[0])
        except IndexError:
            raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f"Order request did not match warehouse state: selected_product_id: {selected_product_id}, selected_size_id: {selected_size_id}, selected_colour_id: {selected_colour_id}, selected_quantity: {selected_quantity}", headers={"X-No-Item": "Product item configuration not found"})
        order.order_quantity = selected_quantity
        order.order_tracking_number = int((_datetime.datetime.now()).strftime('%Y%m%d%H%M%S%f')[:-3]) 
        user_id = get_user_id(db, token)
        await register_order(user_id, order)
        return order