from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import SQLModel, select
from pydantic import BaseModel

from repository.models import ItemDef
from repository.db_connection import delete_db, get_session, engine

class ItemDefDto(BaseModel):
    name: str
    color: str

item_definitions = [
    ItemDefDto(name='Shoes', color='White'),
    ItemDefDto(name='Coat', color='Green'),
    ItemDefDto(name='Hat', color='Black'),
    ItemDefDto(name='Cooler coat', color='Red'),
]

def init_item_defs():
    delete_db()
    SQLModel.metadata.create_all(engine)
    with get_session() as session:
        for dto in item_definitions:
            item_mapped = ItemDef.from_orm(dto)
            session.add(item_mapped)
            session.commit()
            session.refresh(item_mapped)


# item_router = APIRouter()