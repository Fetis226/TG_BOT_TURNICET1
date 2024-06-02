import sqlalchemy as db
import json
import os
import io
import pandas as pd
from encoder import alchemyencoder
from sqlalchemy import create_engine, desc, func
from sqlalchemy.orm import Session
from Models import Person, log, Base, raspisanie_1, raspisanie
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
def Day(Group, Time):
    with Session(autoflush=False, bind=engine) as db:
        print(Group, Time, "group and time-----")
        rasp = db.query(raspisanie).filter(Group == raspisanie.group and raspisanie.start_time.date() ==Time.date()).first()
        print()
        rasp_day = rasp.start_time.strftime('%H%M') + rasp.end_time.strftime('%H%M')
        return(rasp_day)
def check_rasp(status, Time, Group):
    engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
    with Session(autoflush=False, bind=engine) as db:
        print( Time, Group, status)
        if status == True:
            print("WORK1")
            rasp = db.query(raspisanie_1).filter(Group == raspisanie_1.group).first()
            print(rasp.Pon)
            day = datetime.isoweekday(Time)
            print( "day", day)
            rasp_day = Day(Group, Time)
            if rasp_day !=0:
                print('rasp_day----', rasp_day)
                good_time = ""
                Log_time = ""
                log_time = int(Time.strftime('%H%M'))
                if len(str(log_time)) == 4:
                    bol_des = True
                if len(str(log_time)) == 3:
                    bol_des = False
                print(log_time, len(str(log_time)), bol_des)
                if len(str(rasp_day)) < 8:
                    print("WORK1 - entry")
                    print(len(str(rasp_day)))
                    for i in range(3):
                        if i == 1:
                            good_time += str(int(str(rasp_day)[i]) + 3)
                        else:
                            good_time += str(rasp_day)[i]
                        Log_time += str(log_time)[i]
                        print("good time ---",good_time, Log_time)
                    if int(good_time) < int(Log_time):
                        otpr = "Учащийся опоздал"
                        print("aa", otpr)
                        return(otpr)
                    if int(good_time) >= int(Log_time):
                        otpr = "Учащийся вошел в учебное заведение"
                        print("aa", otpr)
                        return(otpr)
                if len(str(rasp_day)) == 8:
                    print('WORK2 - entry')
                    for i in range(4):
                        print("log time----", Log_time)
                        if i == 2:
                            good_time += str(int(str(rasp_day)[i]) + 3)
                        else:
                            good_time += str(rasp_day)[i]
                        if bol_des == False and i < 3:
                            Log_time += str(log_time)[i]
                        if bol_des == True:
                            Log_time += str(log_time)[i]
                        print(good_time)
                        print(Log_time)
                        print("good time ---", good_time)
                    if int(good_time) < int(Log_time):
                        otpr = "Учащийся опоздал"
                        return(otpr)
                    if int(good_time) >= int(Log_time):
                        otpr = "Учащийся вошел в учебное заведение"
                        print("aa", otpr)
                        return(otpr)
            else:
                otpr = "Вход, нет занятий"
                return(otpr)
        elif status == False:
            rasp = db.query(raspisanie_1).filter(Group == raspisanie_1.group).first()
            rasp_day = Day(Group, Time)
            if rasp_day != 0:
                good_time = ""
                Log_time = ""
                log_time = int(Time.strftime('%H%M'))
                print('log time', log_time, len(str(log_time)))
                if len(str(log_time)) == 4:
                    bol_des = True
                if len(str(log_time)) == 3:
                    bol_des = False
                print("Log day", str(log_time), bol_des)
                if len(str(rasp_day)) == 8:
                    print("WORK1-leave")
                    for i in range(4):
                        good_time += str(rasp_day)[4 + i]
                        if bol_des == False and i < 3:
                            Log_time += str(log_time)[i]
                        if bol_des == True:
                            Log_time += str(log_time)[i]
                        print(good_time, Log_time)
                    if int(good_time) <= int(Log_time):
                        otpr = "Учащийся вышел из учебного заведения"
                        print("aa", otpr)
                        return(otpr)
                    if int(good_time) > int(Log_time):
                        otpr = "Учащийся вышел раньше окончания занятий"
                        print("aa", otpr)
                        return(otpr)
                if len(str(rasp_day)) < 8:
                    print("WORK2-leave")
                    for i in range(4):
                        good_time += str(rasp_day)[3 + i]
                        if bol_des == False and i < 3:
                            Log_time += str(log_time)[i]
                        if bol_des == True:
                            Log_time += str(log_time)[i]
                        print(good_time, Log_time)
                    if int(good_time) <= int(Log_time):
                        otpr = "Учащийся вышел из учебного заведения"
                        print("aa", otpr)
                        return(otpr)
                    if int(good_time) > int(Log_time):
                        otpr = "Учащийся вышел раньше окончания занятий"
                        print("aa", otpr)
                        return(otpr)
            else:
                otpr = "Выход, нет занятий"
                return(otpr)