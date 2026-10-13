from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.customer import CustomerDB
from schemas.customer import Customer

MIN_AGE = 18
MAX_AGE = 100
SORT_FIELDS = ["id", "name", "age"]


def check_age(age: int):
    if age < MIN_AGE or age > MAX_AGE:
        raise HTTPException(
            status_code=400,
            detail=f"Age must be between {MIN_AGE} and {MAX_AGE}"
        )


def check_email_available(db: Session, email: str, customer_id: int | None = None):
    query = db.query(CustomerDB).filter(CustomerDB.email == email)
    if customer_id is not None:
        query = query.filter(CustomerDB.id != customer_id)
    if query.first() is not None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )


def create_customer(db: Session, customer: Customer):
    check_age(customer.age)
    check_email_available(db, customer.email)
    db_customer = CustomerDB(
        name=customer.name,
        email=customer.email,
        age=customer.age,
        city=customer.city
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def get_customers(
    db: Session,
    city: str | None = None,
    name: str | None = None,
    sort_by: str = "id",
    order: str = "asc",
    skip: int = 0,
    limit: int = 10
):
    if sort_by not in SORT_FIELDS:
        raise HTTPException(
            status_code=400,
            detail="sort_by must be one of: id, name, age"
        )
    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="order must be asc or desc"
        )
    if skip < 0 or limit < 1 or limit > 100:
        raise HTTPException(
            status_code=400,
            detail="skip must be 0 or more and limit must be between 1 and 100"
        )

    query = db.query(CustomerDB)
    if city:
        query = query.filter(CustomerDB.city == city)
    if name:
        query = query.filter(CustomerDB.name.contains(name))

    column = getattr(CustomerDB, sort_by)
    if order == "desc":
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())

    return query.offset(skip).limit(limit).all()


def get_customer(db: Session, customer_id: int):
    return db.query(CustomerDB).filter(CustomerDB.id == customer_id).first()


def update_customer(db: Session, customer_id: int, updated: Customer):
    customer = get_customer(db, customer_id)
    if customer is None:
        return None
    check_age(updated.age)
    check_email_available(db, updated.email, customer_id)
    customer.name = updated.name
    customer.email = updated.email
    customer.age = updated.age
    customer.city = updated.city
    db.commit()
    db.refresh(customer)
    return customer


def delete_customer(db: Session, customer_id: int):
    customer = get_customer(db, customer_id)
    if customer is None:
        return False
    db.delete(customer)
    db.commit()
    return True
