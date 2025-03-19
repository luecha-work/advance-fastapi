from typing import List
from fastapi import FastAPI, status
from sqlalchemy.sql.functions import mode
from fastapi.params import Depends
from sqlalchemy.orm import Session
from .import schemas
from .import models
from .database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/product/{product_id}", response_model=schemas.DisplayProduct)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.id == product_id).first()
    return product


@app.get("/product", response_model=List[schemas.DisplayProduct])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.put("/product/{product_id}")
def update_product(product_id: int, request: schemas.Product, db: Session = Depends(get_db)):
    product_query = db.query(models.Product).filter(
        models.Product.id == product_id)
    if not product_query.first():
        return {"error": "Product not found"}
    
    # product.name = request.name
    # product.description = request.description
    # product.price = request.price
    # db.commit()
    # db.refresh(product)
    
    product_query.update(request.model_dump())
    db.commit()
    return {"message": "Product updated successfully"}


@app.post("/product", status_code=status.HTTP_201_CREATED)
def create_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name=request.name, description=request.description, price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.delete("/product/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.id == product_id).first()
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
