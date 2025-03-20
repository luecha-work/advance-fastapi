from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from product import models
from product.database import get_db
from product.schemas import LoginRequest

router = APIRouter(prefix="/auth", tags=["Authentication"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.Seller).filter(
        models.Seller.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Username not found/ invalid user")
        
    if not pwd_context.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid Password")
    # Gen JWT Token
    return request

# @router.get("/", response_model=List[schemas.DisplayProduct])
# def get_all_products(db: Session = Depends(get_db)):
#     products = db.query(models.Product).all()
#     return products
