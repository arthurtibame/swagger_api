import base64
import hashlib
import random
from datetime import datetime

from app.Models.APIAuthModel import APIAuth
from app import db
from app.utils.secrets import WhatTheMaskScret
from cryptography.fernet import Fernet

class APIAuthSerivce:

    @staticmethod
    def db_insert_key():
        hashkey = APIAuth.generate_hash_key()
        APIAuth(key=hashkey).add()    
        return {"token": hashkey.decode()}, 200

    @staticmethod
    def db_check_token(token):
        try:                    
            return True if APIAuth.key_check(token) else False
        except Exception as e:
            return False
    
    @staticmethod
    def key_check(key):
        try:
            # check key format
            f = Fernet(WhatTheMaskScret)
            dencrypted = f.decrypt(key.encode()).decode("utf-8")                
            if type(datetime.fromtimestamp(float(dencrypted.split("/")[0]))) is datetime and dencrypted.split("/")[1]=="app":            
                return True
            return False            
        except:
            return False

    @staticmethod
    def generate_token():
        """
        @return: A hashkey for use to authenticate agains the API.
        """
        return base64.b64encode(hashlib.sha256(str(random.getrandbits(256)).encode()).digest(), "mv".encode()).rstrip('=='.encode())


