from sqlalchemy import Column, Integer, String
from .database import Base

class Program(Base):
    __tablename__ = "programs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    subject = Column(String)
