# Session 2: First Real FastAPI Application

## Endpoint

An endpoint is an HTTP method, a path and the Python function that handles the request.

```
GET /customers -> get_customers() -> response
```

- `/customers` is the path (route path).
- `GET` is the HTTP method.
- Together they identify the operation.

## Code

```python
@app.get("/customers")
def get_customers():
    return [
        {"id": 1, "name": "Rahul", "city": "Pune"},
        {"id": 2, "name": "Amit", "city": "Mumbai"}
    ]
```

The data is hardcoded. There is no database yet. Later this is replaced by MySQL through SQLAlchemy.

## Testing

Open `/docs`, select the endpoint, click Try it out, then Execute. No frontend or Postman is needed.

## Mental model

Endpoint = HTTP method + path + Python function that handles the request.

Code: `practice/session_02_customers_endpoint.py`
