from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API is working"}


@app.get("/customers")
def get_customers():
    return [
        {"id": 1, "name": "Rahul", "city": "Pune"},
        {"id": 2, "name": "Amit", "city": "Mumbai"}
    ]


@app.get("/customers/by-city")
def get_customers_by_city(city: str):
    return {"requested_city": city}


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return {"customer_id": customer_id}
