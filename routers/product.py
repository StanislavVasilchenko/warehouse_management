from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from shemas.product import ProductOut, ProductCreate
from configs.db_config import get_db
from crud import product as product_crud

router = APIRouter(prefix="/product", tags=["product"])


@router.post('/', response_model=ProductOut, summary="Create a product")
async def get_products(product: ProductCreate, db: Session = Depends(get_db)):
    return await product_crud.create_product(db, product)


@router.get('/', response_model=List[ProductOut], summary="Get all products")
async def get_products(db: Session = Depends(get_db)):
    return await product_crud.get_all_products(db)
