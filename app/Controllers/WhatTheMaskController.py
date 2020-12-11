from app import ns_WhatTheMask
from flask import request
from flask_restplus import Resource
from app.Services.WhatTheMaskService import WhatTheMaskService
from app.Expects.WhatTheMaskExpect import insert_user_data
from app.utils.decorator import token_required

@ns_WhatTheMask.route('/insert_log')
class Log(Resource):
    @ns_WhatTheMask.expect(insert_user_data)
    @token_required
    def post(self, **kwargs):            
        return WhatTheMaskService.db_insert_log(request)  