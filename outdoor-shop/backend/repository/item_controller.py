from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import SQLModel, select
from pydantic import BaseModel

from repository.models import ItemStock
from repository.db_connection import get_session, engine

import httpx
import random
import requests
import json

class ItemStockDto(BaseModel):
    productId: int
    quantity: int

item_list = []

async def use_cache():
    try:
        url = "http://localhost:8000/api/token"
        response = requests.post(url, data={"username": "230359@edu.p.lodz.pl", "password": "Outdoor"})
        response.raise_for_status()
        return False
    except requests.exceptions.RequestException:
        return True

async def get_items():
    access_token = await get_access_token('230359@edu.p.lodz.pl', 'Outdoor')
    items = await fetch_item_list(access_token)
    list = []
    for item in items:
        details = await fetch_item_details(item['product_id'], access_token)
        for detail in details:
            list.append(detail)
    return list

async def init_item_stocks():
    list = await get_items()
    with get_session() as session:
        for item in list:
            stock_dto = ItemStockDto(productId=item['variation_id'], quantity=random.randint(2, 30))
            item_mapped = ItemStock.from_orm(stock_dto)
            session.add(item_mapped)
            session.commit()
            session.refresh(item_mapped)


item_router = APIRouter()

async def get_access_token(username: str, password: str) -> str:
    url = "http://localhost:8000/api/token"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data={"username": username, "password": password})
        if response.status_code == 200:
            token_data = response.json()
            return token_data["access_token"]
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to get access token")
        
async def fetch_item_list(access_token: str) -> dict:
    url = "http://localhost:8000/api/products/my"
    headers = {"Authorization": f"Bearer {access_token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch items")

async def fetch_item_details(id: int, access_token: str):
    url = "http://localhost:8000/api/products/" + str(id) + "/items"
    headers = {"Authorization": f"Bearer {access_token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch item details")

@item_router.get("/data")
async def get_data():
    global item_list
    cache = await use_cache()
    if cache:
        return item_list
    access_token = await get_access_token('230359@edu.p.lodz.pl', 'Outdoor')
    items = await fetch_item_list(access_token)
    list = []
    for item in items:
        details = await fetch_item_details(item['product_id'], access_token)
        list.append(details)
    item_list = list
    return list

@item_router.get("/images/{id}")
async def get_images(id: int):
    cache = await use_cache()
    if cache:
        data1 = {
            "image_url": "https://www.shutterstock.com/image-vector/no-image-available-vector-illustration-260nw-744886198.jpg"
        }
        data = []
        data.append(data1)
        return data
    access_token = await get_access_token('230359@edu.p.lodz.pl', 'Outdoor')
    url = f'http://localhost:8000/api/products/items/{id}/images'
    headers = {"Authorization": f"Bearer {access_token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch item details")

@item_router.get("/data/{id}")
async def get_data_by_id(id: int):
    cache = await use_cache()
    if cache:
        return [x for x in item_list if x[0]['product_id'] == id][0]
    access_token = await get_access_token('230359@edu.p.lodz.pl', 'Outdoor')
    details = await fetch_item_details(id, access_token)
    return details

@item_router.post('/buy-items')
async def buyItems(item: ItemStockDto):
    with get_session() as session:
        items = session.exec(select(ItemStock)).all()
        for i in items:
            if i.productId == item.productId:
                if i.quantity < item.quantity:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There are not that many items")
                else:
                    setattr(i, 'quantity', i.quantity - item.quantity)
                    session.add(i)
                    session.commit()
                    session.refresh(i)
                    return 'success'
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
@item_router.get('/item-stock', response_model=List[ItemStock])
def get_item_stock():
    with get_session() as session:
        items = session.exec(select(ItemStock)).all()
        return items
    
async def createOrder(id: int):
    access_token = await get_access_token('230359@edu.p.lodz.pl', 'Outdoor')
    url = "http://localhost:8000/api/orders/" + str(1)
    headers = {"Authorization": f"Bearer {access_token}"}

    async with httpx.AsyncClient() as client:
        response = await client.post(url,
        json = {
            "selected_size_id": 1,
            "selected_colour_id": 1,
            "selected_quantity": 1
        },
        headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to create order")
    
@item_router.post('/request-items')
async def makeNeedRequest(dto: ItemStockDto):
    order = await createOrder(dto.productId)
    return 'asd'