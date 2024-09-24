from sqlalchemy.orm import Session
from repositories.products import ProductRepository
from sсhemas.order import OrderItemCreate, OrderUpdate
from repositories.orders import OrdersRepository, OrderItemRepository


async def create_order(db: Session, order: OrderItemCreate):
    order_item_repo = OrderItemRepository(db)
    product_repo = ProductRepository(db)
    try:
        order_item_db = order_item_repo.create(order)
        product_db = product_repo.get_product(product_id=order.product_id)
        if product_db.quantity >= order_item_db.product_quantity:
            product_db.quantity -= order_item_db.product_quantity
            product_repo.save(product_db)
            order_item_repo.save(order_item_db)
            return order_item_db
    except Exception:
        return None


async def get_orders(db: Session):
    return OrdersRepository(db).get_orders()


async def get_order_by_id(db: Session, order_id: int):
    return OrdersRepository(db).get_order(order_id)


async def change_order_status(db: Session, order_id: int, order: OrderUpdate):
    repo_order = OrdersRepository(db)
    order_db = repo_order.get_order(order_id)
    if order_db:
        status = order.status
        order_db.status = status
        repo_order.save(order_db)
        return order_db
