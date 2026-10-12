from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Customer(BaseModel):
    name: str
    age: int
    city: str


@app.get("/")
def home():
    return {"message": "API is working"}


@app.post("/customers")
def create_customer(customer: Customer):
    return {
        "message": "Customer received successfully",
        "customer": customer
    }


@app.get("/customers")
def get_customers():
    return [
        {"id": 1, "name": "Rahul", "age": 25, "city": "Pune"},
        {"id": 2, "name": "Amit", "age": 27, "city": "Mumbai"}
    ]


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return {"customer_id": customer_id}


@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    return {
        "message": "Customer update request received",
        "customer_id": customer_id,
        "updated_data": customer
    }


@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    return {
        "message": "Customer delete request received",
        "customer_id": customer_id
    }
