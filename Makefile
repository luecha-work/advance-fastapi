.PHONY: install server test lint clean

install:
	pip install -r requirements.txt

server:
	uvicorn main:app --reload

# uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
# serve:
# 	fastapi run src/main.py

# serve:
# 	fastapi dev src/main.py

test:
	pytest -v

lint:
	black .
	flake8 .
	isort .

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
