# app/models.py
from sqlalchemy import Column, Integer, String, Float
from app.database.dbConfig import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    department = Column(String)
    salary = Column(Float)
