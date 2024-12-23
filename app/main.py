# app/main.py
from fastapi import FastAPI
from app.routers import employees , std
from app.database.dbConfig import engine
from app.models.empmodel import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(employees.router , tags=["Employees"])
app.include_router(std.router , tags=["Student"])