from models import Product
from schemas import ProductCreate
from database import SessionLocal
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
product_Router=APIRouter(prefix="/Product" ,tags= ["products"])


@product_Router.get('/get')
def get_products(
    db: Session = Depends(get_db)
):
    products = db.query(Product).all()
    return products


@product_Router.get('/{id}')
def get_product_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        return {"message": "product not found"}

    return product


@product_Router.post('/post')
def add_product(product: ProductCreate,db: Session = Depends(get_db)):

    new_product = Product(**product.model_dump())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {
        "message": "product added successfully",
        "product": new_product
    }


@product_Router.put('/put/{id}')
def update_product(
    id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    existing_product = db.query(Product).filter(Product.id == id).first()

    if not existing_product:
        return {"message": "product not found"}

    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.quantity = product.quantity

    db.commit()
    db.refresh(existing_product)

    return {
        "message": "product updated successfully",
        "product": existing_product
    }


@product_Router.delete('/delete/{id}')
def delete_product(
    id: int,
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        return {"message": "product not found"}

    db.delete(product)
    db.commit()

    return {"message": "product deleted successfully"}