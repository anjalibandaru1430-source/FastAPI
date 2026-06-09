from fastapi import APIRouter
from pydantic import BaseModel

products_router = APIRouter(prefix="/products", tags=["products"])

products = [
    {"id": 1, "name": "laptop", "price": 50000},
    {"id": 2, "name": "mobile", "price": 20000},
    {"id": 3, "name": "tablet", "price": 30000}
]

class Product(BaseModel):
    id: int
    name: str
    price: float


@products_router.get("/get")
def get_products():
    return products


@products_router.get("/get/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product["id"] == id:
            return product
    return {"message": "product not found"}


@products_router.post("/create")
def create(product: Product):
    products.append(product.dict())
    return {"message": "product created successfully"}


@products_router.put("/put/{id}")
def update(id: int, updated_product: Product):
    for product in products:
        if product["id"] == id:
            product["name"] = updated_product.name
            product["price"] = updated_product.price
            return {"message": "product updated successfully"}

    return {"message": "product not found"}


@products_router.delete("/delete/{id}")
def delete(id: int):
    for product in products:
        if product["id"] == id:
            products.remove(product)
            return {"message": "product deleted successfully"}

    return {"message": "product not found"}