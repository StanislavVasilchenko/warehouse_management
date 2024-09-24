from typing import List, Type

from models.product import Product
from sqlalchemy.orm import Session

from sсhemas.product import ProductCreate


class ProductRepository:
    def __init__(self, session: Session) -> None:
        self.model = Product
        self.db = session

    def save(self, product: Product) -> Product:
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product: Product) -> Product:
        self.db.delete(product)
        self.db.commit()
        return product

    def create(self, product: ProductCreate) -> Product:
        product = self.model(**product.dict())
        self.save(product)
        return product

    def get_products(self) -> List[Type[Product]]:
        return self.db.query(self.model).all()

    def get_product(self, product_id: int) -> Product:
        return self.db.query(self.model).get(product_id)
