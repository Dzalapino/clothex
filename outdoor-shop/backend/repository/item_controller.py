from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import SQLModel, select
from pydantic import BaseModel

from repository.models import ItemDef, ItemStock
from repository.db_connection import get_session, engine

class ItemDefDto(BaseModel):
    name: str
    color: str

class ItemStockDto(BaseModel):
    productId: int
    quantity: int

item_definitions = [
    ItemDefDto(name='Shoes', color='White'),
    ItemDefDto(name='Coat', color='Green'),
    ItemDefDto(name='Hat', color='Black'),
    ItemDefDto(name='Cooler coat', color='Red'),
]

def init_item_defs():
    SQLModel.metadata.create_all(engine)
    with get_session() as session:
        for dto in item_definitions:
            item_mapped = ItemDef.from_orm(dto)
            session.add(item_mapped)
            session.commit()
            session.refresh(item_mapped)

def init_item_stocks():
    with get_session() as session:
        item_defs = session.exec(select(ItemDef)).all()
        for definition in item_defs:
            stock_dto = ItemStockDto(productId=definition.id, quantity = 1)
            item_mapped = ItemStock.from_orm(stock_dto)
            session.add(item_mapped)
            session.commit()
            session.refresh(item_mapped)



item_router = APIRouter()

@item_router.get('/item-definitions', response_model=List[ItemDef])
def get_all_items_definitions():
    with get_session() as session:
        items = session.exec(select(ItemDef)).all()
        return items

@item_router.get('/item-stock', response_model=List[ItemStock])
def get_item_stock():
    with get_session() as session:
        items = session.exec(select(ItemStock)).all()
        return items