from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.customer import CustomerCreate, CustomerResponse, CustomerUpdate
from app.services import customer_service

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post(
    "",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db),
):
    return customer_service.create_customer(db, customer)


@router.get("", response_model=list[CustomerResponse])
def list_customers(db: Session = Depends(get_db)):
    return customer_service.list_customers(db)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_service.get_customer(db, customer_id)
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found",
        )
    return customer


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int,
    payload: CustomerUpdate,
    db: Session = Depends(get_db),
):
    customer = customer_service.update_customer(db, customer_id, payload)
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found",
        )
    return customer


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    deleted = customer_service.delete_customer(db, customer_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found",
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
