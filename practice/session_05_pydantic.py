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


@app.get("/customers")
def get_customers():
    return [
        {"id": 1, "name": "Rahul", "city": "Pune"},
        {"id": 2, "name": "Amit", "city": "Mumbai"}
    ]


@app.post("/customers")
def create_customer(customer: Customer):
    return {
        "message": "Customer received successfully",
        "customer": customer
    }
