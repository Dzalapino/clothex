"""
This file contains the router for the HQ Products controller.
"""
from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import select

from database.db_connection import get_session
from database.models import HQProduct, LocalProduct


hq_products_router = APIRouter(prefix="/hq_products")


@hq_products_router.get('/', response_model=List[HQProduct])
def get_all_hq_products():
    with get_session() as session:
        hq_products = session.exec(select(HQProduct)).all()
        return hq_products


@hq_products_router.get('/categories', response_model=List[str])
def get_all_categories():
    with get_session() as session:
        categories = session.exec(
            select(HQProduct.category).distinct()
        )
        return categories


@hq_products_router.get('/{hq_product_id}', response_model=HQProduct)
def get_hq_product(hq_product_id: int):
    with get_session() as session:
        hq_product = session.get(HQProduct, hq_product_id)
        if hq_product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HQ product not found")
        return hq_product
