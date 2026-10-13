from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth import verify_token
from database.connection import get_db
from schemas.customer import Customer, CustomerResponse
from services import customer_service

router = APIRouter(prefix="/customers", tags=["customers"])


@router.post(
    "",
    response_model=CustomerResponse,
    status_code=201,
    dependencies=[Depends(verify_token)]
)
def create_customer(customer: Customer, db: Session = Depends(get_db)):
    return customer_service.create_customer(db, customer)


@router.get("", response_model=list[CustomerResponse])
def get_customers(
    city: str | None = None,
    name: str | None = None,
    sort_by: str = "id",
    order: str = "asc",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return customer_service.get_customers(
        db, city, name, sort_by, order, skip, limit
    )


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_service.get_customer(db, customer_id)
    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return customer


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse,
    dependencies=[Depends(verify_token)]
)
def update_customer(
    customer_id: int,
    updated: Customer,
    db: Session = Depends(get_db)
):
    customer = customer_service.update_customer(db, customer_id, updated)
    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return customer


@router.delete(
    "/{customer_id}",
    status_code=204,
    dependencies=[Depends(verify_token)]
)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    deleted = customer_service.delete_customer(db, customer_id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
