from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.customer import CustomerDB
from app.schemas.customer import CustomerCreate, CustomerUpdate


def create_customer(db: Session, payload: CustomerCreate) -> CustomerDB:
    customer = CustomerDB(
        name=payload.name,
        age=payload.age,
        city=payload.city,
    )
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer


def list_customers(db: Session) -> list[CustomerDB]:
    return list(db.scalars(select(CustomerDB).order_by(CustomerDB.id)).all())


def get_customer(db: Session, customer_id: int) -> CustomerDB | None:
    return db.get(CustomerDB, customer_id)


def update_customer(
    db: Session,
    customer_id: int,
    payload: CustomerUpdate,
) -> CustomerDB | None:
    customer = db.get(CustomerDB, customer_id)
    if customer is None:
        return None

    customer.name = payload.name
    customer.age = payload.age
    customer.city = payload.city
    db.commit()
    db.refresh(customer)
    return customer


def delete_customer(db: Session, customer_id: int) -> bool:
    customer = db.get(CustomerDB, customer_id)
    if customer is None:
        return False

    db.delete(customer)
    db.commit()
    return True
