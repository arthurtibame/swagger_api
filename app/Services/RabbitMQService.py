from app.Models.RabbitMQModel import RabbitMQModel
from datetime import datetime

class RabbitMQService:
    @staticmethod
    def publish(json_data):
        message = f"{str(json_data['label'])},{str(json_data['latitude'])},{str(json_data['longitude'])},{datetime.now()}"       
        res = RabbitMQModel(host="172.16.16.40", topic="topic_logs", message=message).basic_publish()       
        if res: 
            return {"status": "Successful" }, 201
        else:
            return {"status": "Failed"}, 404