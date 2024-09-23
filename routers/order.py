from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from configs.db_config import get_db
from shemas.order import OrderItemCreate, OrderItemOut, OrderOut, OrderUpdate
from crud import order as order_crud

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderItemOut, summary="Create a new order")
async def create_order(order: OrderItemCreate, db: Session = Depends(get_db)):
    new_order = await order_crud.create_order(db, order)
    if new_order is None:
        raise HTTPException(status_code=404, detail=f"Product not found")
    return new_order


@router.get("/", response_model=List[OrderOut])
async def get_orders(db: Session = Depends(get_db)):
    return await order_crud.get_orders(db)


@router.get("{order_id}", response_model=OrderOut)
async def get_order(order_id: int, db: Session = Depends(get_db)):
    order_db = await order_crud.get_order_by_id(db, order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail=f"Order #{order_id} not found")
    return order_db


@router.patch("/{order_id}/status", response_model=OrderOut)
async def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    order_db = await order_crud.change_order_status(db, order_id, order)
    if order_db is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order_db
