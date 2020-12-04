from app import db
from datetime import datetime

class Log(db.Model):
    __tablename__ = 'Log'    
    id = db.Column(db.Integer,primary_key=True)
    label = db.Column(db.String(16))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    CreateTime = db.Column(db.DateTime, default=datetime.utcnow)
    ModifyTime = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, label, latitude, longitude):
        self.label  = label
        self.latitude = latitude
        self.longitude = longitude

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def find_by_name(cls, name):
        return cls.filter_by(name == name).first()        


