from pydantic import BaseModel, ConfigDict


class Customer(BaseModel):
    name: str
    email: str
    age: int
    city: str


class CustomerResponse(Customer):
    id: int
    model_config = ConfigDict(from_attributes=True)
