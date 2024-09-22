from sqlalchemy.orm import Session
from shemas.product import ProductCreate
from models.product import Product


async def create_product(db: Session, product: ProductCreate):
    product = Product(**product.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


async def get_all_products(db: Session):
    return db.query(Product).all()


async def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).get(int(product_id))
