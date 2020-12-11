from app.Models.WhatTheMaskModel import Log
from app import db

def db_insert_log(request):
    try:
        json_data=request.json
        Log(
            userid = json_data['userid'],
            label=json_data['label'],
            location = json_data['location'],
            latitude=json_data['latitude'],
            longitude=json_data['longitude'],            

        ).add()             

        return {"status":"Successful"}, 201
    except:
        return {"status": "Failed"}, 404
