from app import ns_RabbitMQ
from flask import request
from flask_restplus import Resource
from app.Services.RabbitMQService import RabbitMQService
from app.Expects.WhatTheMaskExpect import insert_user_data
from app.utils.decorator import token_required

@ns_RabbitMQ.route('/insert_log')
class Log(Resource):
    @ns_RabbitMQ.expect(insert_user_data)
    @token_required
    def post(self, **kwargs):            
        return RabbitMQService.publish(request.json)  