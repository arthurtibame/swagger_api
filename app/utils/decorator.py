from flask import request
from functools import wraps
from app.Services.APIAuthService import APIAuthSerivce

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwards):
        token = None
        if 'token' in request.json:
            token = request.json['token']
        if not token:
            return {'message': 'Token required'}, 401
        if APIAuthSerivce.db_check_token(token) != True:
            return {'message': 'Wrong token'}, 401        
        return func(*args, **kwards)
    return decorated

def generate_token_check(func):
    @wraps(func)
    def decorated(*args, **kwards):
        key = None
        if 'key' in request.json:
            key = request.json['key']
        if not key:
            return {"message": "key required"}, 401     
        if APIAuthSerivce.key_check(key) != True:
            return {'message': 'Wrong key'}, 401
        return func(*args, **kwards)
    return decorated

        