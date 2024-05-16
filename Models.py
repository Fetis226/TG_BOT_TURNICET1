from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String, DateTime, ForeignKey, Boolean
import datetime
class Base(DeclarativeBase): pass


class Person(Base):
    __tablename__ = "stud-par"

    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    parent_name = Column(String)
    parent_id = Column(Integer)
    code = Column(String, unique= True)
    group_id = Column(Integer)
class log(Base):
    __tablename__ = "log"
    idlog = Column(Integer, primary_key=True, index=True, autoincrement= True)
    date = Column(DateTime)
    entry_id = Column(Integer, index= True)
    Status = Column(Boolean, default= False)
class raspisanie_1(Base):
    __tablename__ = "raspisanie_1"
    idrasp = Column(Integer, primary_key= True, index= True, autoincrement= True)
    Pon = Column(Integer, default=0)
    Vto = Column(Integer, default=0)
    Sre = Column(Integer, default=0)
    Che = Column(Integer, default=0)
    Pt = Column(Integer, default=0)
    sub = Column(Integer, default=0)
    group = Column(Integer, default=0)