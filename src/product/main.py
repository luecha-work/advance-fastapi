from fastapi import FastAPI
from .schemas import Product

app = FastAPI()


@app.post("/product")
def create_product(request: Product):
    return request
