from fastapi import FastAPI, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

# Learn CORS

#Initializes FastAPI application
app = FastAPI()

#List of allowed origins for CORS
origins = [
    'http://localhost:5173'
]

# Add CORS middleware to the FastApi application
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'],allow_headers=['*'])


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

@app.post("/transactions/", response_model=TransactionModel)
async def create_transaction(transaction: TransactionBase, db : db_dependecy):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@app.get("/transactions/",response_model=List[TransactionModel])
async def read_transactions(db: db_dependecy, skip: int = 0 ,limit:int = 100):
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions






