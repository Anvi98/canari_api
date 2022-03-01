import json
from numpy import percentile
import psycopg2
from sqlalchemy import and_
from fastapi import Depends, FastAPI
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from app import models, database
from . import utils, database, models


models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()


file = 'test'

# utils.normalization(file)

try:
  conn = psycopg2.connect(host='localhost', database='canari', user='postgres', port='5433', password='root12', cursor_factory=RealDictCursor)
  cursor = conn.cursor()
  print("Connection to DB sucessfull ...")
except Exception as error:
  print("Connecting to database.")
  print("Error:", error)

@app.get("/")
async def root():
    return {"message": "Hello to Canari"}
  
@app.get("/search")
async def search(stack: str, city: str, db: Session = Depends(database.get_db)):
  # companies = db.query(models.Company).filter(and_(models.Company.stack.contains(stack), models.Company.city==city)).all()
  number = db.query(models.Company).filter(and_(models.Company.stack.contains(stack), models.Company.city==city)).count()
  total = db.query(models.Company).count()
  percentage = (number * 100)/total

  return {"percent": f'{percentage}%', "match number": number, "total Comp": total }

@app.get("/testy")
def comp(db: Session = Depends(database.get_db)):

  return {"DB": "Db working"}