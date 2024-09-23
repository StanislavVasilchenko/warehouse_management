from sqlalchemy.orm import Session

from models.product import Product
from sсhemas.order import OrderItemCreate, OrderUpdate
from models.order import Order, OrderItem


async def create_order_in_db(db: Session):
    order = Order()
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


async def create_order(db: Session, order: OrderItemCreate):
    order_item_db = OrderItem(**order.dict())

    if order.order_id == 0:
        order_db = await create_order_in_db(db)
        order_item_db.order_id = order_db.id

    prod_db = db.query(Product).get(order_item_db.product_id)
    if prod_db and prod_db.quantity >= order_item_db.product_quantity:
        prod_db.quantity = prod_db.quantity - order_item_db.product_quantity
        db.add(prod_db)
        db.add(order_item_db)
        db.commit()
        db.refresh(order_item_db)
        return order_item_db


async def get_orders(db: Session):
    return db.query(Order).all()


async def get_order_by_id(db: Session, order_id: int):
    order_item_db = db.query(Order).get(int(order_id))
    return order_item_db


async def change_order_status(db: Session, order_id: int, order: OrderUpdate):
    order_item_db = await get_order_by_id(db, order_id)
    if order_item_db:
        status = order.status
        order_item_db.status = status
        db.commit()
        db.refresh(order_item_db)
        return order_item_db
