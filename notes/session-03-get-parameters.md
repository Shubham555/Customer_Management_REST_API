# Session 3: GET APIs, Path Parameters and Query Parameters

## Path parameter

Identifies a specific resource.

```python
@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return {"customer_id": customer_id}
```

- `{customer_id}` is a variable in the URL.
- FastAPI passes the value into the function.
- `int` means an integer is expected.

Examples: `/customers/1`, `/customers/25`, `/orders/500`.

## Query parameter

Filters, searches, sorts or paginates.

```python
@app.get("/customers/by-city")
def get_customers_by_city(city: str):
    return {"requested_city": city}
```

Example: `/customers/by-city?city=Pune`. The `?` starts the query parameters.

## Comparison

| Path parameter | Query parameter |
| --- | --- |
| `/customers/1` | `/customers/by-city?city=Pune` |
| Identifies a specific customer | Specifies a filter or option |
| `customer_id` | `city` |

In this session the city endpoint only returns the requested city. It does not filter real records.

Code: `practice/session_03_parameters.py`
