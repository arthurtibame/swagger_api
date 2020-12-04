from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from app.utils import setting

flask_app = Flask(__name__)
flask_app.config.from_object(setting) 

api = Api(app = flask_app,
          version="1.0"  ,
          title="Modovision Apis",
          description="Manage names of various apps api of the application"          
)

# Register namespace
ns_WhatTheMask = api.namespace('WhatTheMask', description='WhatTheMask android app APIs')
ns_APIAuth = api.namespace('auth', description='Auth')

# Db connector
db = SQLAlchemy(flask_app)

from app.Controllers import WhatTheMaskController, APIAuthController
from app.Expects import WhatTheMaskExpect
from app.Models import WhatTheMaskModel, APIAuthModel
from app.Services import WhatTheMaskService, APIAuthService
