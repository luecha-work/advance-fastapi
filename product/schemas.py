from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: int
    seller_id: int

    class Config:
        orm_mode = True


class Seller(BaseModel):
    username: str
    email: str
    password: str


class DisplaySeller(BaseModel):
    username: str
    email: str


class DisplayProduct(BaseModel):
    name: str
    description: str
    seller: DisplaySeller

    class Config:
        orm_mode = True
        
class LoginRequest(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None