from fastapi import FastAPI
from routers.product import router as product_router
from routers.order import router as order_router


app = FastAPI()

app.include_router(product_router)
app.include_router(order_router)


@app.on_event("startup")
async def startup():
    from configs.db_config import engine, Base
    from models.product import Product  # noqa
    from models.order import Order, OrderItem  # noqa

    Base.metadata.create_all(bind=engine)
