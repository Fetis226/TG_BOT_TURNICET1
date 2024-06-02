from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import  Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy_serializer import SerializerMixin
import datetime
class Base(DeclarativeBase, SerializerMixin): pass
class Person(Base):
    __tablename__ = "stud-par"

    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    parent_name = Column(String, default='0')
    parent_id = Column(Integer, default='0')
    code = Column(String, unique= True, default='0')
    group_id = Column(Integer, default=0)
    student_name = Column(String, default='0')
    Group = Column(String, default='0')

class log(Base):
    __tablename__ = "log"
    idlog = Column(Integer, primary_key=True, index=True, autoincrement= True)
    date = Column(DateTime)
    entry_id = Column(Integer, index= True)
    Status = Column(Boolean, default= False)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
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
class raspisanie(Base):
    __tablename__ = "raspisanie"
    rasp_id = Column(Integer, primary_key= True, index= True, autoincrement= True)
    start_time = Column(DateTime, default=0)
    end_time = Column(DateTime, default=0)
    group = Column(Integer,default=0)
