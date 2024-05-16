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