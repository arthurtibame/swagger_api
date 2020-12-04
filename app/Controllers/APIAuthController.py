from flask import request
from app import ns_APIAuth
from flask_restplus import Resource
from app.Services.APIAuthService import APIAuthSerivce
from app.utils.decorator import generate_token_check

@ns_APIAuth.route('/token', doc=False)
class GenerateToken(Resource):
    @generate_token_check  
    def get(self, **kwargs):            
        return APIAuthSerivce.db_insert_key() 