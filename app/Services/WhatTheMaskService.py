from app.Models.WhatTheMaskModel import Log
from app import db

def db_insert_log(json_data):
    try:              
        Log(
            label=json_data['label'],
            latitude=json_data['latitude'],
            longitude=json_data['longitude'],            
        ).add()             

        return {"status":"Successful"}, 201
    except:
        return {"status": "Failed"}, 404
