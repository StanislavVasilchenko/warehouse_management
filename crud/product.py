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
