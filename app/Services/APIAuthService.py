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
        """[summary]
        Returns:
            [dict]: [return token to the user calling api 
                     and also insert the generated has key to db
                    ]
            [web status]:  [200 (successful)]                    
        """
        hashkey = APIAuth.generate_hash_key()
        APIAuth(key=hashkey).add()    
        return {"token": hashkey.decode()}, 200

    @staticmethod
    def db_check_token(token):
        """[summary]

        Args:
            token ([byte]): [the key from the user sent if the format is available]

        Returns:
            [boolean]: [if the key is the right format return True else False]
        """
        try:                    
            return True if APIAuth.check_key(token) else False
        except Exception as e:
            return False
    
    @staticmethod
    def check_key(key):
        """[summary]

        Args:
            key ([byte]): [the key from user sent]

        Returns:
            [Boolean]: [if the format is timestamp/app then return True else false]
        
        Notes:
            In the future, if adding the  namespace of api which is calling from PC user  then adding 
            the rule here ->　Timestamp/web ...etc
        """
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


