from fastapi import FastAPI,APIRouter

product_router=APIRouter(prefix="/products",tags=["users"])
products=[
  {
    "id": 1,
    "name": "Wireless Mouse",
    "category": "Electronics",
    "price": 799,
    "stock": 50,
    "brand": "Logitech"
  },
  {
    "id": 2,
    "name": "Mechanical Keyboard",
    "category": "Electronics",
    "price": 2499,
    "stock": 30,
    "brand": "Redragon"
  },
  {
    "id": 3,
    "name": "Bluetooth Headphones",
    "category": "Electronics",
    "price": 1999,
    "stock": 25,
    "brand": "Boat"
  },
  {
    "id": 4,
    "name": "Smart Watch",
    "category": "Wearables",
    "price": 3499,
    "stock": 20,
    "brand": "Noise"
  },
  {
    "id": 5,
    "name": "Gaming Laptop",
    "category": "Computers",
    "price": 74999,
    "stock": 10,
    "brand": "ASUS"
  },
  {
    "id": 6,
    "name": "USB-C Charger",
    "category": "Accessories",
    "price": 999,
    "stock": 100,
    "brand": "Anker"
  },
  {
    "id": 7,
    "name": "External SSD",
    "category": "Storage",
    "price": 5499,
    "stock": 15,
    "brand": "Samsung"
  },
  {
    "id": 8,
    "name": "Office Chair",
    "category": "Furniture",
    "price": 6999,
    "stock": 12,
    "brand": "Green Soul"
  },
  {
    "id": 9,
    "name": "Water Bottle",
    "category": "Home",
    "price": 499,
    "stock": 80,
    "brand": "Milton"
  },
  {
    "id": 10,
    "name": "Running Shoes",
    "category": "Fashion",
    "price": 2999,
    "stock": 40,
    "brand": "Puma"
  }
]
@product_router.get("/get")
def get():
    for product in products:
     return products
    return {"products not found"}
@product_router.get("/get/{id}")
def get(id:int):
   for product in products:
      if product["id"]==id:
         return product
      return {"msg":"product not found"}
    
@product_router.post("/create")
def create():

    return {"msg": "products created"}
@product_router.put("/update")
def update():
    return {"msg":"product updated successfully"}
@product_router.delete("/delete")
def delete():
    return {"msg":"product deleted successfully"}