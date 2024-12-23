# app/schemas.py
from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    age: int
    department: str
    salary: float

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    name: str
    age: int
    grade: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
