from fastapi import FastAPI
from Routes.products import product_router
app=FastAPI()
@app.get("/index")
def index():
    return {"this is index page"}

app.include_router(product_router)