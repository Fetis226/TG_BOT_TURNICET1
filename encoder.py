import datetime
import sqlalchemy as db
import json
import os
import io
import pandas as pd
from sqlalchemy import create_engine, desc, func
from sqlalchemy.orm import Session
from Models import Person, log, Base, raspisanie_1, raspisanie
metadata = db.MetaData()
engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, str):
    	return obj.strip()
def export_log():
    l = open('txt.txt', "r")
    last_id = int(l.read())
    with Session(autoflush=False, bind=engine) as db:
        with open('json.json', 'w') as f:
            Log = db.query(log).filter(log.idlog > last_id).order_by(log.idlog).all()
            print(Log)
            os.remove("outputs1.xlsx")
            result_dict = [row.__dict__ for row in Log]
            print(result_dict)
            pd.DataFrame(result_dict).to_excel('outputs1.xlsx')
            f.close()
def update_student():
    with Session(autoflush=False, bind=engine) as db:
        with io.open('студенты.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            print(json_data)

            stud_par = db.query(Person).all()
            for i in json_data:
                print(json_data.get(i))
                db.add(Person(**json_data[i]))
                db.commit()
            json_data.clear()
            db.commit()
            print(json_data)
def update_raspisanie():
    with Session(autoflush=False, bind=engine) as db:
        with io.open('расписание.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            a=0
            for i in json_data:
                print(json_data.get(i))
                if i == "start_time":
                    print(i, json_data[i].get("start_time"), "time")
                    json_data[i].update(start_time = datetime.datetime.strptime(str(json_data[i].get("start_time")), '%Y-%m-%dT%H:%M:%S'))
                if i == "end_time":
                    json_data[i].update(end_time=datetime.datetime.strptime(str(json_data[i].get("end_time")), '%Y-%m-%dT%H:%M:%S'))
                db.add(raspisanie(**json_data[i]))
                db.commit()
            json_data.clear()