from sqlalchemy import Column, Integer, String
from database.connection import Base


class CustomerDB(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    city = Column(String(100), nullable=False)
