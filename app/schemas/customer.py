from pydantic import BaseModel, ConfigDict, Field


class CustomerCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=130)
    city: str = Field(min_length=1, max_length=100)


class CustomerUpdate(CustomerCreate):
    # PUT replaces the customer's editable fields.
    pass


class CustomerResponse(CustomerCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
