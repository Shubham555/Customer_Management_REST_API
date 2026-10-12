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


@app.post("/customers")
def create_customer(data: dict):
    return {
        "message": "Customer received successfully",
        "customer": data
    }
