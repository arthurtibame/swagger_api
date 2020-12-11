from datetime import datetime
from app import db
import base64
import hashlib
import random

class APIAuth(db.Model):
    __tablename__  = 'APIAuth'
    id = db.Column(db.Integer,primary_key=True)
    key = db.Column(db.LargeBinary)    
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    modifytime = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, key):
        self.key = key
   
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def key_check(cls, key):                                
        return db.session.query(cls.key).filter(cls.key==key.encode()).one()
          
    @staticmethod
    def generate_hash_key():
        """
        @return: A hashkey for use to authenticate agains the API.
        """
        return base64.b64encode(hashlib.sha256(str(random.getrandbits(256)).encode()).digest(), "mv".encode()).rstrip('=='.encode())


