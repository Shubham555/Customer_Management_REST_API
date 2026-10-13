from fastapi import FastAPI

from database.connection import engine, Base
from models.customer import CustomerDB
from routers import customers, external

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(customers.router)
app.include_router(external.router)


@app.get("/")
def home():
    return {"message": "API is working"}
