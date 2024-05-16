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
def rassilka(i):
    engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
    l = open('txt.txt')
    last_id = int(l.read())
    print(last_id)
    with Session(autoflush=False, bind=engine) as db:
        print(i)
        print("new_id", last_id+1)
        logstatus_first = db.query(log).filter(log.idlog > last_id).order_by(log.idlog).first()
        print(logstatus_first.entry_id)
        Log = db.query(Person).filter(logstatus_first.entry_id == Person.id).first()
        print("log_parent", logstatus_first.entry_id, Log.id)
        print("idlog-", logstatus_first.idlog)
        print("status-", logstatus_first.Status)
        print("id-", logstatus_first.entry_id)
        Time = logstatus_first.date
        status = logstatus_first.Status
        idlog = logstatus_first.idlog
        enter = logstatus_first.entry_id
        par_id = Log.parent_id
        Group = Log.group_id
        print(par_id)
        return (enter, status, par_id, idlog, Time, Group, engine)
def rewrite_id(idlog):
    k = open("txt.txt", "w")
    k.write(str(idlog))
def check():
    engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
    l = open('txt.txt', "r")
    last_id = int(l.read())
    print(last_id)
    with Session(autoflush=False, bind=engine) as db:
        Log = db.query(log)
        try:
            logstatus = db.query(log).filter(log.idlog > last_id).order_by(log.idlog)
            row_count = db.query(log).filter(log.idlog > last_id).order_by(log.idlog.desc()).count()
            print("row count -",row_count)
        finally:
            pass
        if row_count == 0:
            Success = False
        else:
            Success = True
        return (row_count, Success)