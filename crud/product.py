from sqlalchemy.orm import Session
from sсhemas.product import ProductCreate, ProductUpdate
from models.product import Product
from repositories.products import ProductRepository


async def create_product(product: ProductCreate, db: Session) -> Product:
    return ProductRepository(db).create(product)


async def get_all_products(db: Session):
    return ProductRepository(db).get_products()


async def get_product_by_id(db: Session, product_id: int):
    return ProductRepository(db).get_product(product_id)


async def product_update(db: Session, product: ProductUpdate, product_id: int):
    repos = ProductRepository(db)
    product_db = repos.get_product(product_id)
    if product_db:
        for key, value in vars(product).items():
            setattr(product_db, key, value) if value else None
        return repos.save(product_db)


async def delete_product(db: Session, product_id: int):
    repos = ProductRepository(db)
    product_db = repos.get_product(product_id)
    if product_db:
        return repos.delete(product_db)
