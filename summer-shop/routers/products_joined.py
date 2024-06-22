"""
File for the endpoints responsible for the local_products joined with the hq_products
"""
from fastapi import APIRouter, HTTPException, status
from typing import List
from sqlmodel import select

from database.db_connection import get_session
from database.models import LocalProduct as LocalProductModel, HQProduct as HQProductModel
from database.schemas import HQLocalJoined


products_joined_router = APIRouter(prefix='/products_joined')


@products_joined_router.get('/', response_model=List[HQLocalJoined])
def get_all_local_products_joined():
    with get_session() as session:
        # Construct the query to select required fields
        query = select(LocalProductModel, HQProductModel).join(HQProductModel)

        # Execute the query and fetch all results
        result = session.exec(query).all()

        # Map the results to HQLocalJoined objects
        joined_products = []
        for lp_model, hq_model in result:
            joined_product = HQLocalJoined(
                id=lp_model.id,
                hq_product_id=lp_model.hq_product_id,
                category=hq_model.category,
                name=hq_model.name,
                image_url=hq_model.image_url,
                description=hq_model.description,
                price_pln=hq_model.price_pln,
                amount_in_stock=lp_model.amount_in_stock,
            )
            joined_products.append(joined_product)

        return joined_products


@products_joined_router.get('/{local_product_id}', response_model=HQLocalJoined)
def get_local_product_joined(local_product_id: int):
    with (get_session() as session):
        query = select(LocalProductModel, HQProductModel).join(
            HQProductModel).where(LocalProductModel.id == local_product_id)
        result = session.exec(query).first()

        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Local product with id {local_product_id} not found")

        lp_model, hq_model = result

        joined_product = HQLocalJoined(
            id=lp_model.id,
            hq_product_id=lp_model.hq_product_id,
            category=hq_model.category,
            name=hq_model.name,
            image_url=hq_model.image_url,
            description=hq_model.description,
            price_pln=hq_model.price_pln,
            amount_in_stock=lp_model.amount_in_stock,
        )

        return joined_product
