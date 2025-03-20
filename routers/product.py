from typing import List
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from product import models, schemas
from product.database import get_db

router = APIRouter( tags=["Products"])


@router.get("/product/{product_id}", response_model=schemas.DisplayProduct, tags=["Products"])
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    return product


@router.get("/product", response_model=List[schemas.DisplayProduct])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products


@router.put("/product/{product_id}", tags=["Products"])
def update_product(product_id: int, request: schemas.Product, db: Session = Depends(get_db)):
    product_query = db.query(models.Product).filter(
        models.Product.id == product_id)
    if not product_query.first():
        return {"error": "Product not found"}

    product_query.update(request.model_dump())
    db.commit()
    return {"message": "Product updated successfully"}


@router.post("/product", status_code=status.HTTP_201_CREATED)
def create_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name=request.name, description=request.description, price=request.price, seller_id=request.seller_id)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.delete("/product/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.id == product_id).first()
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
