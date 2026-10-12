from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

from database import engine, SessionLocal, Base
from models import CustomerDB

app = FastAPI()

Base.metadata.create_all(bind=engine)


class Customer(BaseModel):
    name: str
    age: int
    city: str


class CustomerResponse(Customer):
    id: int
    model_config = ConfigDict(from_attributes=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "API is working"}


@app.post("/customers", response_model=CustomerResponse)
def create_customer(customer: Customer, db: Session = Depends(get_db)):
    db_customer = CustomerDB(
        name=customer.name,
        age=customer.age,
        city=customer.city
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


@app.get("/customers", response_model=list[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    return db.query(CustomerDB).all()


@app.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(CustomerDB).filter(CustomerDB.id == customer_id).first()
    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return customer


@app.put("/customers/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: int, updated: Customer, db: Session = Depends(get_db)):
    customer = db.query(CustomerDB).filter(CustomerDB.id == customer_id).first()
    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    customer.name = updated.name
    customer.age = updated.age
    customer.city = updated.city
    db.commit()
    db.refresh(customer)
    return customer


@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(CustomerDB).filter(CustomerDB.id == customer_id).first()
    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    db.delete(customer)
    db.commit()
    return {"message": "Customer deleted successfully"}
