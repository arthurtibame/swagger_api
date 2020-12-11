from app import db
from datetime import datetime

class Log(db.Model):
    __tablename__ = 'Log'    
    id = db.Column(db.Integer,primary_key=True)
    userid = db.Column(db.String(50))
    label = db.Column(db.String(50))
    location = db.Column(db.String(50))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    modifytime = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, userid, label,location, latitude, longitude):
        self.userid=userid
        self.label=label
        self.location=location
        self.latitude=latitude
        self.longitude=longitude

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def find_by_name(cls, name):
        return cls.filter_by(name == name).first()        


