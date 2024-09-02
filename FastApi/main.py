from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

# Learn CORS

#Initializes FastAPI application
app = FastAPI()

#List of allowed origins for CORS
origins = []

# Add CORS middleware to the FastApi application
app.add_middleware(CORSMiddleware, allow_origins=origins)


# Base Model for transactions using pydantic
class TransactionBase(BaseModel):
    amount:float
    category:str
    description:str
    is_income:bool
    date:str

class TransactionModel(TransactionBase):
    id: int

    class Config:
        orm_mode = True # Allows compatibility with SQLAlchemy models



# Dependency function to provide database session
def get_db():
    db = SessionLocal() # This creates new database session
    try:
        yield db # Yields the session to be used by dependencies
    finally:
        db.close() #Ensures the session is closed after use


db_dependecy = Annotated[Session, Depends(get_db)]

# Creates db tables based on SQLAlchemy models
models.Base.metadata.create_all(bind = engine)


