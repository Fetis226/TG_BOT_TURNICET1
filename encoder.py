import datetime
import sqlalchemy as db
import json
import os
import io
import copy
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Models import Person, log, raspisanie
metadata = db.MetaData()
engine = create_engine("mysql+pymysql://root:2266@localhost/gaga")
def alchemyencoder(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, str):
    	return obj.strip()
def export_log():
    l = open('txt.txt', "r")
    last_id = int(l.read())
    os.remove("outputs1.xlsx")
    with Session(autoflush=False, bind=engine) as db:
        with open('json.json', 'w') as f:
            Log = db.query(log).filter(log.idlog > last_id).order_by(log.idlog).all()
            result_dict = [row.__dict__ for row in Log]
            result_dict_copy = copy.deepcopy(result_dict)
            if not result_dict == False:
                a=0
                for i in list(result_dict_copy):
                    for j in i:
                        if j == "_sa_instance_state":
                            result_dict[a].pop(j)
                    a+=1
                    if a+1 > len(result_dict):
                        break
                a=0
                for i in result_dict:
                    for j in i:
                        if j =="date":
                            result_dict[a].update(date=result_dict[a].get("date").strftime('%d-%m-%Y %H:%M:%S'))
                    a+=1
                    if a + 1 > len(result_dict):
                        break
                pd.DataFrame(result_dict).to_excel('outputs1.xlsx')
            if not result_dict == True:
                f.close()
def update_student():
    with Session(autoflush=False, bind=engine) as db:
        with io.open('студенты.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            a=0
            for i in json_data:
                for j in i:
                    db.add(Person(**json_data[a]))
                    db.commit()
                    a += 1
                if a+1>len(json_data):
                    break
            json_data.clear()

def update_raspisanie():
    with Session(autoflush=False, bind=engine) as db:
        with io.open('расписание.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            a=0
            for i in json_data:
                for j in i:
                    if j == "start_time":
                        json_data[a].update(start_time=datetime.datetime.strptime(str(json_data[a].get("start_time")),
                                                                                  '%Y-%m-%dT%H:%M:%S'))
                    if j == "end_time":
                        json_data[a].update(
                            end_time=datetime.datetime.strptime(str(json_data[a].get("end_time")), '%Y-%m-%dT%H:%M:%S'))
                    db.add(raspisanie(**json_data[a]))
                    db.commit()
                    a += 1
                if a+1>len(json_data):
                    break
            json_data.clear()
