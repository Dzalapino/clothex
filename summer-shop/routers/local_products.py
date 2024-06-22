"""
This module contains the routers for the local_products endpoints
"""
from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import select

from database.db_connection import get_session
from database.models import LocalProduct as LocalProductModel, HQProduct as HQProductModel
from database.schemas import LocalProduct as LocalProductSchema, HQLocalJoined


local_products_router = APIRouter(prefix='/local_products')


@local_products_router.get('/', response_model=List[LocalProductModel])
def get_all_local_products():
    with get_session() as session:
        local_products = session.exec(select(LocalProductModel)).all()
        return local_products


@local_products_router.get('/{local_product_id}', response_model=LocalProductModel)
def get_local_product(local_product_id: int):
    with get_session() as session:
        local_product = session.get(LocalProductModel, local_product_id)
        if local_product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Local product not found")
        return local_product


@local_products_router.post('/', response_model=LocalProductModel)
def create_local_product(local_product: LocalProductSchema):
    with get_session() as session:
        local_product_mapped = LocalProductModel.from_orm(local_product)
        session.add(local_product_mapped)
        session.commit()
        session.refresh(local_product_mapped)
        return local_product_mapped


@local_products_router.patch('/{local_product_id}/{amount}', response_model=LocalProductModel)
def increment_amount_in_stock(local_product_id: int, amount: int):
    with get_session() as session:
        local_product = session.get(LocalProductModel, local_product_id)
        if local_product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Local product not found")
        local_product.amount_in_stock += amount
        session.add(local_product)
        session.commit()
        session.refresh(local_product)
        return local_product


@local_products_router.delete('/{local_product_id}', response_model=LocalProductModel)
def delete_local_product(local_product_id: int):
    with get_session() as session:
        local_product = session.get(LocalProductModel, local_product_id)
        if local_product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Local product not found")
        session.delete(local_product)
        session.commit()
        return local_product
