# Session 4: POST Requests, Request Body and JSON

## Request body

The data sent by the client to the API.

```json
{
  "name": "Priya",
  "age": 24,
  "city": "Pune"
}
```

## POST endpoint

```python
@app.post("/customers")
def create_customer(data: dict):
    return {
        "message": "Customer received successfully",
        "customer": data
    }
```

- `@app.post("/customers")` creates a POST endpoint.
- `data: dict` receives the request body as a Python dictionary.
- FastAPI parses the JSON for you.
- Nothing is saved yet. The endpoint returns the submitted data.

## GET vs POST

| GET | POST |
| --- | --- |
| Retrieves data | Submits or creates data |
| Filters often in the URL | Data often in the request body |
| `GET /customers` | `POST /customers` |

The same path can be used by both. The HTTP method decides the operation.

Code: `practice/session_04_post_request.py`
