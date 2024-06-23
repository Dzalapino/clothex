#fastapi-jwt/main.py
from typing import List
import fastapi as _fastapi
import fastapi.security as _security

import sqlalchemy.orm as _orm
 
import services as _services, schemas as _schemas
 
from datetime import timedelta as _timedelta

app = _fastapi.FastAPI()
"""
@app.post("/api/users")
async def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    db_user = await _services.get_user_by_email(user.email, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Email already in use")
 
    user = await _services.create_user(user, db)
 
    return await _services.create_token(user)
"""
 
@app.post("/api/token")
async def generate_token(
    form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(),
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    user = await _services.authenticate_user(form_data.username, form_data.password, db)
 
    if not user:
        raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    
    access_token_expires = _timedelta(minutes=_services.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await _services.create_access_token(user, expires_delta=access_token_expires)
    return access_token

@app.get("/api/myprofile", response_model=_schemas.User)
async def get_user(user: _schemas.User = _fastapi.Depends(_services.get_current_user)):
    return user


@app.get("/api/myproducts", response_model=_schemas.ProductsList)
async def get_user_products(products: _schemas.ProductsList = _fastapi.Depends(_services.get_user_products)):
    return products

@app.get("/api/selected_product_items/{selected_product_id}", response_model=_schemas.ProductsItemsList)
async def get_selected_product_items(selected_product_id: int, product_items: _schemas.ProductsItemsList = _fastapi.Depends(_services.get_selected_product_items)):
    if len(product_items)>1:
        return product_items
    else:
        raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_403_FORBIDDEN,
                            detail="Product item id not found for your license", headers={"WWW-Authenticate": "Bearer"})
    
@app.get("/api/order_product_item/{selected_product_id}/{selected_product_variation_id}/{selected_quantity}", response_model=_schemas.ProductOrder)
async def order_product_item(selected_product_id: int, selected_size_id: int, selected_colour_id: int, selected_quantity: int, 
                             order: _schemas.ProductOrder = _fastapi.Depends(_services.get_selected_product_items)):
    if 0 < order.order_quantity <= order.quantity_in_stock:
        return order
    else:
        raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f"Invalid order size: {order}", headers={"WWW-Authenticate": "Bearer"})