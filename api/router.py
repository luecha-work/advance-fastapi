from fastapi import APIRouter
from .import product, seller, auth

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(product.router)
api_router.include_router(seller.router)