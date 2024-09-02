from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

# Learn CORS

app = FastAPI()
origins = []
app.add_middleware(CORSMiddleware, allow_origins=origins)

class TransactionBase(BaseModel):
    amount:float
    category:str
    description:str
    is_income:bool
    date:str

class TransactionModel(TransactionBase):
    id: int

    class Config:
        orm_mode = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
