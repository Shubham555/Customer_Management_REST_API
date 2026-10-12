# Session 5: Pydantic and Data Validation

## Why

With `data: dict`, a client could send `"age": "banana"` or leave out `name`. Pydantic defines the expected structure and validates incoming values.

## Model

```python
from pydantic import BaseModel


class Customer(BaseModel):
    name: str
    age: int
    city: str
```

## Using it in an endpoint

```python
@app.post("/customers")
def create_customer(customer: Customer):
    return {
        "message": "Customer received successfully",
        "customer": customer
    }
```

## Flow

```
Client -> POST /customers -> FastAPI -> Pydantic validation -> Python function -> Response
```

## Behaviour

- Valid data: the function runs and the response is returned.
- `"age": "banana"`: FastAPI returns `422 Unprocessable Entity` and the function does not run.
- Missing `name`: validation error, because the field is required.
- Compatible values such as `"25"` can be converted to the integer `25`.

Pydantic validates incoming data. SQLAlchemy (later) talks to MySQL. They have different responsibilities.

Code: `practice/session_05_pydantic.py`
