from app import ns_WhatTheMask
from flask_restplus import fields

insert_user_data = ns_WhatTheMask.model("Insert_user_data",
                                 {
                                    "label": 
fields.String(description="label", required=True),
                                    "latitude": 
fields.String(description="latitude", required=True),
                                    "longitude": 
fields.String(description="longitude", required=True),
                                    "token": 
fields.String(description="token", required=True),
                                 }
                                )