import json
from numpy import percentile
import psycopg2
from sqlalchemy import and_
from fastapi import Depends, FastAPI
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from app import models, database
from . import utils, database, models
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

origins = ["*"]
app.add_middleware(
  CORSMiddleware,
  allow_origins= origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


file = 'test'

# utils.normalization(file)

@app.get("/")
async def root():
    return {"message": "Hello to Canari"}

@app.get("/testy")
def comp(db: Session = Depends(database.get_db)):

  return {"DB": "Db working"}
  
@app.get("/search")
async def search(stack: str, city: str, db: Session = Depends(database.get_db)):
  #companies = db.query(models.Company).filter(and_(models.Company.stack.contains(stack), models.Company.city==city)).all()
  number = db.query(models.Company).filter(and_(models.Company.stack.contains(stack), models.Company.city.contains(city))).count()
  total = db.query(models.Company).count()
  total_companies_city = db.query(models.Company).filter(models.Company.city.contains(city)).count()
  percentage = (number * 100)/total_companies_city

  return {"percent": f'{percentage}%', "match number": number, f"total Companies in {city}": total_companies_city, "total companies": total }

