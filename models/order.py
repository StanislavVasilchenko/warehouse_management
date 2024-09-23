from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum as EnumPy
from datetime import datetime

from configs.db_config import Base


class OrderSatus(EnumPy):
    in_process = 'in_process'
    sent = "sent"
    delivered = "delivered"


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_creation = Column(DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), index=True)
    status = Column(Enum(OrderSatus), default=OrderSatus.in_process)

    order_items = relationship("OrderItem", back_populates="orders")


class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), index=True)
    product_id = Column(Integer, ForeignKey('product.id'), index=True)
    product_quantity = Column(Integer, index=True)

    orders = relationship('Order')
    product = relationship('Product')
