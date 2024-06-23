from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import SQLModel, select
from pydantic import BaseModel

from repository.models import ItemDef, ItemStock
from repository.db_connection import get_session, engine

class ItemDefDto(BaseModel):
    name: str
    color: str
    imgUrl: str

class ItemStockDto(BaseModel):
    productId: int
    quantity: int

item_definitions = [
    ItemDefDto(name='Shoes', color='White', imgUrl='buty.jpg'),
    ItemDefDto(name='Coat', color='Green', imgUrl='kurtka.jpg'),
    ItemDefDto(name='Hat', color='Black', imgUrl='czapka.jpg'),
    ItemDefDto(name='Cooler coat', color='Red', imgUrl='kurtka2.jpg'),
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
            stock_dto = ItemStockDto(productId=definition.id, quantity = 10)
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

@item_router.post('/buy-items')
def buyItems(item: ItemStockDto):
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

@item_router.get('/item/{id}', response_model=ItemDef) 
def get_item_by_id(id: int):
    with get_session() as session:
        item = session.get(ItemDef, id)
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return item