import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Models import Person, log, raspisanie_1, raspisanie
from datetime import *
metadata = db.MetaData()
engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
def parent_log_reg(data):
    engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
    with Session(autoflush=False, bind=engine) as db:
        stud_id = db.query(Person).filter(Person.id == int(f'{data["ID"]}')).first()
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
    with Session(autoflush=False, bind=engine) as db:
        logstatus_first = db.query(log).filter(log.idlog > last_id).order_by(log.idlog).first()
        Log = db.query(Person).filter(logstatus_first.entry_id == Person.id).first()
        Time = logstatus_first.date
        status = logstatus_first.Status
        idlog = logstatus_first.idlog
        enter = logstatus_first.entry_id
        par_id = Log.parent_id
        Group = Log.group_id
        return (enter, status, par_id, idlog, Time, Group, engine)
def rewrite_id(idlog):
    k = open("txt.txt", "w")
    k.write(str(idlog))
def check():
    engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
    l = open('txt.txt', "r")
    last_id = int(l.read())
    with Session(autoflush=False, bind=engine) as db:
        Log = db.query(log)
        try:
            logstatus = db.query(log).filter(log.idlog > last_id).order_by(log.idlog)
            row_count = db.query(log).filter(log.idlog > last_id).order_by(log.idlog.desc()).count()
        finally:
            pass
        if row_count == 0:
            Success = False
        else:
            Success = True
        return (row_count, Success)
def Day(Group, Time):
    with Session(autoflush=False, bind=engine) as db:
        rasp = db.query(raspisanie).filter(Group == raspisanie.group and raspisanie.start_time.date() ==Time.date()).first()
        rasp_day = rasp.start_time.strftime('%H%M') + rasp.end_time.strftime('%H%M')
        return(rasp_day)
def check_rasp(status, Time, Group):
    engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
    with Session(autoflush=False, bind=engine) as db:
        if status == True:
            rasp = db.query(raspisanie_1).filter(Group == raspisanie_1.group).first()
            day = datetime.isoweekday(Time)
            rasp_day = Day(Group, Time)
            if rasp_day !=0:
                good_time = ""
                Log_time = ""
                log_time = int(Time.strftime('%H%M'))
                if len(str(log_time)) == 4:
                    bol_des = True
                if len(str(log_time)) == 3:
                    bol_des = False
                if len(str(rasp_day)) < 8:
                    for i in range(3):
                        if i == 1:
                            good_time += str(int(str(rasp_day)[i]) + 3)
                        else:
                            good_time += str(rasp_day)[i]
                        Log_time += str(log_time)[i]
                    if int(good_time) < int(Log_time):
                        otpr = "Учащийся опоздал"
                        return(otpr)
                    if int(good_time) >= int(Log_time):
                        otpr = "Учащийся вошел в учебное заведение"
                        return(otpr)
                if len(str(rasp_day)) == 8:
                    for i in range(4):
                        if i == 2:
                            good_time += str(int(str(rasp_day)[i]) + 3)
                        else:
                            good_time += str(rasp_day)[i]
                        if bol_des == False and i < 3:
                            Log_time += str(log_time)[i]
                        if bol_des == True:
                            Log_time += str(log_time)[i]
                    if int(good_time) < int(Log_time):
                        otpr = "Учащийся опоздал"
                        return(otpr)
                    if int(good_time) >= int(Log_time):
                        otpr = "Учащийся вошел в учебное заведение"
                        return(otpr)
            else:
                otpr = "Вход, нет занятий"
                return(otpr)
        elif status == False:
            rasp_day = Day(Group, Time)
            if rasp_day != 0:
                good_time = ""
                Log_time = ""
                log_time = int(Time.strftime('%H%M'))
                if len(str(log_time)) == 4:
                    bol_des = True
                if len(str(log_time)) == 3:
                    bol_des = False
                if len(str(rasp_day)) == 8:
                    for i in range(4):
                        good_time += str(rasp_day)[4 + i]
                        if bol_des == False and i < 3:
                            Log_time += str(log_time)[i]
                        if bol_des == True:
                            Log_time += str(log_time)[i]
                    if int(good_time) <= int(Log_time):
                        otpr = "Учащийся вышел из учебного заведения"
                        return(otpr)
                    if int(good_time) > int(Log_time):
                        otpr = "Учащийся вышел раньше окончания занятий"
                        return(otpr)
                if len(str(rasp_day)) < 8:
                    for i in range(4):
                        good_time += str(rasp_day)[3 + i]
                        if bol_des == False and i < 3:
                            Log_time += str(log_time)[i]
                        if bol_des == True:
                            Log_time += str(log_time)[i]
                    if int(good_time) <= int(Log_time):
                        otpr = "Учащийся вышел из учебного заведения"
                        return(otpr)
                    if int(good_time) > int(Log_time):
                        otpr = "Учащийся вышел раньше окончания занятий"
                        return(otpr)
            else:
                otpr = "Выход, нет занятий"
                return(otpr)