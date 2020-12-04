import os
#调试模式是否开启
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
#session必须要设置key
SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'




SQLALCHEMY_DATABASE_URI = r"mysql+pymysql://root:2020aiot@172.16.16.40:3306/android_app"