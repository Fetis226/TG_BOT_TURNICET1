import sqlalchemy as db
from sqlalchemy import create_engine, desc, func
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import Session
from Models import Person, log, Base, raspisanie_1
from datetime import *
metadata = db.MetaData()
engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
def parent_log_reg(data):
    engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
    with Session(autoflush=False, bind=engine) as db:
        stud_id = db.query(Person).filter(Person.id == int(f'{data["ID"]}')).first()
        print(stud_id)
        if stud_id.code == f'{data["code"]}':
            stud_id.parent_name = f'{data["parent_name"]}'
            stud_id.parent_id = f'{data["parent_id"]}'
            db.commit()
        else:
            print("Пользователь уже в системе")
def entry(argue):
    engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
    print("success")
    with Session(autoflush=False, bind=engine) as db:
        Log = db.query(log)
        Log.date = datetime.now()
        Log.entry_id = argue
        Log.Status = False
        logstatus = db.query(log).filter(log.entry_id == Log.entry_id).order_by(log.idlog.desc()).first()
        if logstatus == None:
            Log.Status = True
        else:
            if logstatus.Status == True:
                Log.Status = False
            elif logstatus.Status == False:
                Log.Status = True
        logadd = log(
            date = Log.date,
            entry_id = Log.entry_id,
            Status = Log.Status
        )
        db.add(logadd)
        db.commit()
        db.close()