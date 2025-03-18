# fastapi-project

This is a FastAPI project that provides an API for retrieving a list of books.

## Project Structure

```
fastapi-project
├── src
│   ├── app.py          # Main entry point of the FastAPI application
│   └── requirements.txt # Lists project dependencies
├── Makefile            # Automation commands for the project
├── .env                # Environment variables for configuration
└── README.md           # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:
   ```
   make serve
   ```

## Usage

Once the application is running, you can access the API at `http://localhost:8000/books` to retrieve the list of books.

# FastAPI Tutorial & Installation Guide

## Introduction
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to be easy to use, and it is ideal for building scalable web applications.

## Features
- **Fast**: Asynchronous and high-performance, powered by Starlette and Pydantic.
- **Easy to use**: Simple and intuitive API design.
- **Automatic validation**: Uses Python type hints for automatic data validation.
- **Interactive API documentation**: Swagger UI and ReDoc are built-in.

## Installation
To install FastAPI, you need to have Python 3.7 or later installed.

### Step 1: Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv env

source env/bin/activate  # On macOS and Linux

env\Scripts\activate    # On Windows
```

### Step 2: Install FastAPI and Uvicorn
FastAPI does not include a built-in web server, so you need to install Uvicorn (an ASGI server) as well.
```sh
pip install fastapi uvicorn

or 

pip install uvicorn[standard]
```

## Creating a Simple FastAPI Application
Create a file called `main.py` and add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

## Running the Application
Use Uvicorn to start the FastAPI server:
```sh
uvicorn main:app --reload
```

- The `--reload` flag enables automatic code reloading on changes.
- The default port is `8000`. You can access the API at `http://127.0.0.1:8000`.

## Interactive API Documentation
FastAPI provides automatic API documentation with Swagger UI and ReDoc:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Adding Path Parameters
Modify `main.py` to include a path parameter:
```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```
Now, accessing `http://127.0.0.1:8000/items/10` will return:
```json
{"item_id": 10}
```

## Request Body Example
FastAPI supports automatic request body validation using Pydantic models:
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
```

## Conclusion
FastAPI is a powerful framework for building modern APIs with minimal effort. It provides fast performance, automatic validation, and interactive documentation, making API development efficient and enjoyable.

For more details, visit the official documentation: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com).

