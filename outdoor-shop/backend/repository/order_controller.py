# from typing import List
# from fastapi import APIRouter
# from pydantic import BaseModel
# from sqlmodel import SQLModel, select

# from repository.models import ItemStock, Order
# from repository.db_connection import get_session, engine

# class OrderDto(BaseModel):
#     items: List[ItemStock]

# order_router = APIRouter()

# @order_router.get('/orders', response_model=List[Order])
# def get_all_orders():
#      with get_session() as session:
#         orders = session.exec(select(Order)).all()
#         return orders
     
# @order_router.post('/orders', response_model=List[Order])
# def create_order(order: OrderDto):
#     with get_session() as session:
#         order_mapped = Order.from_orm(order)
#         session.add(order_mapped)
#         session.commit()
#         session.refresh(order_mapped)
#         return order_mapped