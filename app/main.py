from fastapi import FastAPI

from app.database import Base, engine
from app.models.customer import CustomerDB
from app.routers.customers import router as customers_router

app = FastAPI(
    title="Customer Management REST API",
    description="A beginner-friendly REST API built with FastAPI and MySQL.",
    version="1.0.0",
)

# Create tables that do not exist yet. Larger applications should use migrations.
Base.metadata.create_all(bind=engine)

app.include_router(customers_router)


@app.get("/", tags=["Health"])
def home():
    return {"message": "Customer Management API is running"}
