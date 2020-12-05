from app.Models.WhatTheMaskModel import Log
from app import db

class WhatTheMaskService:
    @staticmethod
    def db_insert_log(json_data):
        """[summary]

        Args:
            json_data ([dict]): [The data from the user sent which will be insert to database]

        Returns:
            [dict]: [the responses 201 or 404]
        """
        try:              
            Log(
                label=json_data['label'],
                latitude=json_data['latitude'],
                longitude=json_data['longitude'],            
            ).add()             

            return {"status":"Successful"}, 201
        except:
            return {"status": "Failed"}, 404
