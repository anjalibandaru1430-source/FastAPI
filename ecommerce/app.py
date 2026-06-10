from fastapi import FastAPI
from Routes.products import product_Router

from database import engine, Base
from models import Product

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/')
def index_page():
    return {"message": "this is index page"}

app.include_router(product_Router)
