from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_restful import Api
from datetime import datetime
from app.db_table import db
from flask_restful import reqparse, abort, Api, Resource
from app.api.ExceptionApi import ExceptionTableApi, ExceptionModifyApi, ExceptionListApi
from app.cron.RecordException import scheduler

app = Flask(__name__)
app.config.from_object('config')
app.config['JSON_AS_ASCII'] = False
pymysql.install_as_MySQLdb()

db.init_app(app)
with app.app_context():
    from app.db_table.exception_table import *
    db.create_all()

scheduler.init_app(app)
scheduler.start()

api = Api(app)

api.add_resource(ExceptionModifyApi, '/api/exception')
api.add_resource(ExceptionListApi, '/api/exception/list')
api.add_resource(ExceptionTableApi, '/api/exception/delete')

app.run(debug=True)