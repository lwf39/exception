from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_restful import Api
from datetime import datetime
from app.db_table import db
from flask_restful import reqparse, abort, Api, Resource
from app.api.ExceptionApi import ExceptionTableApi



app = Flask(__name__)
app.config.from_object('config')

pymysql.install_as_MySQLdb()

db.init_app(app)
with app.app_context():
    from app.db_table.exception_table import *
    db.create_all()


api = Api(app)

api.add_resource(ExceptionTableApi, '/')

app.run()