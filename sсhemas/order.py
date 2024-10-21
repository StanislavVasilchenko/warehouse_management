from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from models.order import OrderSatus


class OrderBase(BaseModel):
    status: OrderSatus = OrderSatus.in_process


class OrderItemsBase(BaseModel):
    order_id: int
    product_id: int
    product_quantity: int


class OrderItemCreate(OrderItemsBase):
    order_id: Optional[int] = None
    product_id: int
    product_quantity: int


class OrderItemOut(OrderItemsBase):
    id: int
    order_id: int

    class Config:
        orm_mode = True


class OrderOut(OrderBase):
    date_creation: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id: int
    order_items: List[OrderItemOut]

    class Config:
        orm_mode = True


class OrderUpdate(OrderBase):
    status: OrderSatus
