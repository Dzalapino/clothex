from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import select

from database.db_connection import get_session
from database.models import LocalProduct as LocalProductModel
from database.schemas import LocalProduct as LocalProductSchema


local_products_router = APIRouter()


@local_products_router.get('/local_products/', response_model=List[LocalProductModel])
def get_all_local_products():
    with get_session() as session:
        local_products = session.exec(select(LocalProductModel)).all()
        return local_products


@local_products_router.post('/local_products/', response_model=LocalProductModel)
def create_local_product(local_product: LocalProductSchema):
    with get_session() as session:
        local_product_mapped = LocalProductModel.from_orm(local_product)
        session.add(local_product_mapped)
        session.commit()
        session.refresh(local_product_mapped)
        return local_product_mapped


# TODO: Implement patch for amount in stock


@local_products_router.delete('/local_products/{local_product_id}', response_model=LocalProductModel)
def delete_local_product(local_product_id: int):
    with get_session() as session:
        local_product = session.get(LocalProductModel, local_product_id)
        if local_product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Local product not found")
        session.delete(local_product)
        session.commit()
        return local_product
