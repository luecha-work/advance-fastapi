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
