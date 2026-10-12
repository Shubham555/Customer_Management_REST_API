from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()


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
