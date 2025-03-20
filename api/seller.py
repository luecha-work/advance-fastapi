from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from product import models, schemas
from product.database import get_db
from passlib.context import CryptContext

router = APIRouter(prefix="/seller",tags=["Sellers"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/", response_model=schemas.DisplaySeller)
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(
        username=request.username, email=request.email, password=hashed_password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller

@router.get("/{seller_id}", response_model=schemas.DisplaySeller)
def get_seller(seller_id: int, db: Session = Depends(get_db)):
    seller = db.query(models.Seller).filter(
        models.Seller.id == seller_id).first()
    if not seller:
        return {"error": "Seller not found"}
    return seller
