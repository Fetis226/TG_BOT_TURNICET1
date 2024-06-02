import datetime
import sqlalchemy as db
import json
import os
import io
import copy
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
    os.remove("outputs1.xlsx")
    with Session(autoflush=False, bind=engine) as db:
        with open('json.json', 'w') as f:
            Log = db.query(log).filter(log.idlog > last_id).order_by(log.idlog).all()
            result_dict = [row.__dict__ for row in Log]
            print(result_dict)
            result_dict_copy = copy.deepcopy(result_dict)
            if not result_dict == False:
                print(result_dict)
                a=0
                for i in list(result_dict_copy):
                    for j in i:
                        print(j, a,"<>", len(result_dict))
                        if j == "_sa_instance_state":
                            result_dict[a].pop(j)
                        print(result_dict[a])
                    a+=1
                    if a+1 > len(result_dict):
                        break
                a=0
                print(result_dict,"CHECK LENGHT", len(result_dict))
                for i in result_dict:
                    for j in i:
                        if j =="date":
                            print(j)
                            result_dict[a].update(date=result_dict[a].get("date").strftime('%d-%m-%Y %H:%M:%S'))
                        print("---- final",j, a, "<>", len(result_dict), result_dict[a], result_dict,"--- final")
                    a+=1
                    if a + 1 > len(result_dict):
                        break
                print(result_dict,"final result dict")
                pd.DataFrame(result_dict).to_excel('outputs1.xlsx')
            if not result_dict == True:
                print("Обновлений нет")
            f.close()
def update_student():
    with Session(autoflush=False, bind=engine) as db:
        with io.open('студенты.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            print(json_data)
            a=0
            for i in json_data:
                for j in i:
                    print(j)
                    db.add(Person(**json_data[a]))
                    db.commit()
                    a += 1
                if a+1>len(json_data):
                    break
            json_data.clear()
            print(json_data)

def update_raspisan():
    with Session(autoflush=False, bind=engine) as db:
        with io.open('расписание.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            print(json_data)
            a=0
            for i in json_data:
                print(i,"dict")
                for j in i:
                    print(a, "<>", len(json_data))
                    print(j, "---j")
                    print(json_data[a], "dict--dict")
                    if j == "start_time":
                        print(json_data[a],"dict--dict")
                        print(j, json_data[a].get("start_time"), "time")
                        json_data[a].update(start_time=datetime.datetime.strptime(str(json_data[a].get("start_time")),
                                                                                  '%Y-%m-%dT%H:%M:%S'))
                    if j == "end_time":
                        json_data[a].update(
                            end_time=datetime.datetime.strptime(str(json_data[a].get("end_time")), '%Y-%m-%dT%H:%M:%S'))
                    print(json_data, "--- finallo")
                    db.add(raspisanie(**json_data[a]))
                    db.commit()
                    a += 1
                if a+1>len(json_data):
                    break
            json_data.clear()
export_log()