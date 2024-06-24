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
async def user(user: _schemas.User = _fastapi.Depends(_services.get_current_user)):
    return user

@app.get("/api/brands/{selected_brand_id}", response_model=_schemas.BrandDetails)
async def brand_details(brand_details: _schemas.BrandDetails = _fastapi.Depends(_services.get_brand_details)):
    return brand_details

@app.get("/api/products/my", response_model=_schemas.ProductsList)
async def user_products(products: _schemas.ProductsList = _fastapi.Depends(_services.get_user_products)):
    return products

@app.get("/api/products/{selected_product_id}/items", response_model=_schemas.ProductsItemsList)
async def selected_product_items(selected_product_id: int, product_items: _schemas.ProductsItemsList = _fastapi.Depends(_services.get_selected_product_items)):
    if len(product_items)>1:
        return product_items
    else:
        raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_403_FORBIDDEN,
                            detail="Product item id not found for your license", headers={"X-No-Item": "Product item not found"})
    
@app.get("/api/products/items/{selected_item_id}/images", response_model=_schemas.ProductItemImagesList)
async def selected_item_images(selected_item_id: int, item_images: _schemas.ProductItemImagesList = _fastapi.Depends(_services.get_item_images)):
    return item_images

@app.post("/api/orders/{selected_product_item_id}/{selected_variant_id}/{selected_quantity}", response_model=_schemas.ProductOrder)
async def order_product_item(order: _schemas.ProductOrder = _fastapi.Depends(_services.make_item_order), user: _schemas.User = _fastapi.Depends(_services.get_current_user)):
    if 0 < order.order_quantity <= order.quantity_in_stock:
        subject = "We have received your order"
        msg = f"We got your order, Wait for confirmation! Here are your order details: {order}"
        recipent=user.email
        email = _schemas.EmailContent(recipent=recipent,subject=subject, message=msg)
        await _services.send_email(email)
        return order
    else:
        raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f"Order request did not match warehouse state: {order}", headers={"X-No-Item": "Product item configuration not found"})