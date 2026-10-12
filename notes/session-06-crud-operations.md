# Session 6: CRUD Operations

| Letter | Operation | Method and path |
| --- | --- | --- |
| C | Create | `POST /customers` |
| R | Read | `GET /customers`, `GET /customers/1` |
| U | Update | `PUT /customers/1` |
| D | Delete | `DELETE /customers/1` |

## Update

```python
@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    return {
        "message": "Customer update request received",
        "customer_id": customer_id,
        "updated_data": customer
    }
```

- `customer_id` comes from the URL path.
- `customer: Customer` is the validated request body.

## Delete

```python
@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    return {
        "message": "Customer delete request received",
        "customer_id": customer_id
    }
```

In this session these endpoints are demonstrations. They do not change stored data. Real database operations come in Session 7.

## Architecture

```
Client -> FastAPI endpoint -> Validation + Python logic -> Database -> HTTP response
```

Code: `practice/session_06_crud_demo.py`
