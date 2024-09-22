from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup():
    from configs.db_config import engine, Base
    from models.product import Product  # noqa
    Base.metadata.create_all(bind=engine)
