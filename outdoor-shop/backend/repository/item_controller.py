from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import SQLModel, select

from repository.models import ItemStock
from repository.db_connection import get_session, engine
# from repository.item_service import fetch_item_details, fetch_item_list, get_access_token, createOrder, use_cache, ItemStockDto
from repository.item_service import *

import httpx


item_list = []

item_router = APIRouter()

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
    
@item_router.post('/request-items')
async def makeNeedRequest(dto: ItemStockDto):
    cache = await use_cache()
    if cache:
        raise HTTPException(status_code=500, detail="HQ not available")
    product_id = 1
    for items in item_list:
        for x in items:
            if x['variation_id'] == dto.productId:
                product_id = x['product_id']
    order = await createOrder(product_id, dto.productId, dto.quantity)
    return order