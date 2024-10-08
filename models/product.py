from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import relationship

from configs.db_config import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(Text)
    price = Column(Float, index=True)
    quantity = Column(Integer, index=True)

    order_items = relationship("OrderItem", back_populates="product")
