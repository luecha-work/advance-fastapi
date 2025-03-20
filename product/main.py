from typing import List
from fastapi import FastAPI, HTTPException, Response, status
from sqlalchemy.sql.functions import mode
from fastapi.params import Depends
from sqlalchemy.orm import Session
from .import schemas
from .import models
from .database import engine, SessionLocal
from passlib.context import CryptContext

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/product/{product_id}", response_model=schemas.DisplayProduct)
def get_product(product_id: int, response: Response, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
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

    product_query.update(request.model_dump())
    db.commit()
    return {"message": "Product updated successfully"}


@app.post("/product", status_code=status.HTTP_201_CREATED)
def create_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name=request.name, description=request.description, price=request.price, seller_id=request.seller_id)
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


@app.post('/seller', response_model=schemas.DisplaySeller)
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(
        username=request.username, email=request.email, password=hashed_password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller

