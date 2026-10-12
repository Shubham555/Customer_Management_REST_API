from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    if customer_id != 1:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    return {
        "id": 1,
        "name": "Rahul",
        "age": 25,
        "city": "Pune"
    }
