from fastapi import FastAPI

import api
from . import models
from .database import engine
from api import router

tags_metadata = [
    {
        "name": "Products",
        "description": "Endpoints related to products"
    },
    {
        "name": "Sellers",
        "description": "Endpoints related to sellers"
    }
]

app = FastAPI(
    title="Product API",
    description="A simple API to manage products and sellers",
    terms_of_service="http://www.google.com/",
    version="0.0.1",
    contact={
        "developer Name": "luecha kanmaneekul",
        "website": "http://www.google.com/",
        "email": "demo@gmail.com"
    },
    license_info={
        "name": "XYZ License",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
    openapi_tags=tags_metadata
)
app.include_router(router.api_router)

models.Base.metadata.create_all(bind=engine)
