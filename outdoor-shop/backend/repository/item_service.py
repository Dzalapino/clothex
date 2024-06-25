
import httpx
import random
import requests
from fastapi import HTTPException
from repository.db_connection import get_session, engine
from pydantic import BaseModel
from repository.models import ItemStock

class ItemStockDto(BaseModel):
    productId: int
    quantity: int

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

async def createOrder(id: int, variant_id: int, quantity: int):
    access_token = await get_access_token('230359@edu.p.lodz.pl', 'Outdoor')
    url = f'http://localhost:8000/api/orders/{id}/{variant_id}/{quantity}'
    headers = {"Authorization": f"Bearer {access_token}"}

    print(url)

    async with httpx.AsyncClient() as client:
        response = await client.post(url, data={}, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to create order")