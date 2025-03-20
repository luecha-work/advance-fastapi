import datetime
from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from product import models
from product.database import get_db
from product.schemas import LoginRequest

SECRET_KEY = "8ef337392c1ee90ecafa529003619cfc49c4695b53c1855fa819fcdece5a82de"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

router = APIRouter(prefix="/auth", tags=["Authentication"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_token(data: dict) -> str:
    payload = data.copy()
    expire = datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


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
