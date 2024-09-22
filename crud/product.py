from sqlalchemy.orm import Session
from shemas.product import ProductCreate, ProductUpdate
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


async def product_update(db: Session, product: ProductUpdate, product_id: int):
    product_db = db.query(Product).get(int(product_id))
    if product_db is not None:
        for var, value in vars(product).items():
            setattr(product_db, var, value) if value else None
        db.commit()
        db.refresh(product_db)
        return product_db
