from typing import List, Type

from sqlalchemy.orm import Session
from models.order import Order, OrderItem
from sсhemas.order import OrderItemCreate


class OrdersRepository:
    def __init__(self, db: Session) -> None:
        self.order = Order
        self.db = db

    def save(self, order: Order) -> Order:
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def create(self, order: Order = Order()) -> Order:
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def get_orders(self) -> List[Type[Order]]:
        return self.db.query(Order).all()

    def get_order(self, order_id: int) -> Order:
        return self.db.query(Order).get(order_id)


class OrderItemRepository:
    def __init__(self, db: Session) -> None:
        self.order_item = OrderItem
        self.db = db

    def save(self, order_item: OrderItem) -> OrderItem:
        self.db.add(order_item)
        self.db.commit()
        self.db.refresh(order_item)
        return order_item

    def create(self, order_item: OrderItemCreate) -> OrderItem:
        if order_item.order_id == 0:
            order = OrdersRepository(self.db).create()
            order_item_db = self.order_item(**order_item.dict())
            order_item_db.order_id = order.id
            self.save(order_item_db)
            return self.save(order_item_db)
        return self.save(self.order_item(**order_item.dict()))
