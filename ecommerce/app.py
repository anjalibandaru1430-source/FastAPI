from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from Routes.products import products_router
import models
from database import SessionLocal, engine
from models import Product
from schemas import ProductCreate, ProductResponse

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(products_router)



# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Home Route
@app.get("/")
def index_page():
    return {"message": "Product API Running Successfully"}


# Create Product
@app.post("/create/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(
        name=product.name,
        price=product.price
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


# Get All Products
@app.get("/read/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


# Get Product By ID
@app.get("/read/{id}", response_model=ProductResponse)
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    return product


# Update Product
@app.put("/update/{id}", response_model=ProductResponse)
def update_product(
    id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(Product.id == id).first()

    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    db_product.name = product.name
    db_product.price = product.price

    db.commit()
    db.refresh(db_product)

    return db_product


# Delete Product
@app.delete("/delete/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == id).first()

    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    db.delete(db_product)
    db.commit()

    return {"message": "Product Deleted Successfully"}