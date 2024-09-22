from sqlalchemy import Column, Integer, String, Text

from configs.db_config import Base


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(Text)
    price = Column(Integer, index=True)
    quantity = Column(Integer, index=True)
