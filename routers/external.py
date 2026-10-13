import httpx
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth import verify_token
from database.connection import get_db
from schemas.customer import Customer, CustomerResponse
from services import customer_service

router = APIRouter(tags=["external"])

USERS_URL = "https://jsonplaceholder.typicode.com/users"


async def fetch_external_user(user_id: int):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{USERS_URL}/{user_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="External service request failed"
        )


@router.get("/external-user/{user_id}")
async def get_external_user(user_id: int):
    return await fetch_external_user(user_id)


@router.post(
    "/customers/import/{user_id}",
    response_model=CustomerResponse,
    status_code=201,
    dependencies=[Depends(verify_token)]
)
async def import_customer(
    user_id: int,
    age: int,
    db: Session = Depends(get_db)
):
    user = await fetch_external_user(user_id)
    customer = Customer(
        name=user["name"],
        email=user["email"],
        age=age,
        city=user["address"]["city"]
    )
    return customer_service.create_customer(db, customer)
