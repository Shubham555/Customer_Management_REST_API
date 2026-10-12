# Session 10: External API Integration

An external API is another system our application calls and uses the response from.

```
Client -> Our FastAPI -> External API -> Our FastAPI -> Client
```

## Setup

```
pip install httpx
```

## Example

Uses `https://jsonplaceholder.typicode.com/users/1`.

```python
@app.get("/external-user/{user_id}")
async def get_external_user(user_id: int):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="External service request failed"
        )
```

## Key points

- `httpx.AsyncClient` sends HTTP requests.
- `await client.get(url)` calls the external API and waits for the response without blocking the event loop.
- `response.raise_for_status()` raises an error for unsuccessful statuses.
- `response.json()` converts the JSON response to Python data.
- `502` tells our client that our API could not get a successful response from the upstream service.

## GenAI connection

The same idea applies when a backend calls an LLM provider, an embedding service or a vector database.

Code: `practice/session_10_external_api.py`
