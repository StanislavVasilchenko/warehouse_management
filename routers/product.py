from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from shemas.product import ProductOut, ProductCreate, ProductUpdate
from configs.db_config import get_db
from crud import product as product_crud

router = APIRouter(prefix="/products", tags=["product"])


@router.post('/', response_model=ProductOut, summary="Create a product")
async def get_products(product: ProductCreate, db: Session = Depends(get_db)):
    return await product_crud.create_product(db, product)


@router.get('/', response_model=List[ProductOut], summary="Get all products")
async def get_products(db: Session = Depends(get_db)):
    return await product_crud.get_all_products(db)


@router.get('/{id}', response_model=ProductOut, summary="Get a product by id")
async def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = await product_crud.get_product_by_id(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    return db_product


@router.put('/{id}', response_model=ProductOut, summary="Update a product by id")
async def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    prod_db = await product_crud.product_update(db, product, product_id)
    if prod_db is None:
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    return prod_db
