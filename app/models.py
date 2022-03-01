from sqlalchemy import Column, Float, Integer, String, Boolean
from .database import Base

class Company(Base):
  __tablename__ = "companies"

  id = Column(Integer, primary_key=True, nullable=False)
  companyName = Column(String, nullable=False)
  website = Column(String, nullable=False)
  address = Column(String, nullable=False)
  city = Column(String, nullable=False)
  state = Column(String, nullable=False)
  stack = Column(String, nullable=False)
  zip = Column(Integer, nullable=False)
  latitude = Column(Float, nullable=False)
  longitude = Column(Float, nullable=False)
  companyDescription = Column(String, nullable=False)
