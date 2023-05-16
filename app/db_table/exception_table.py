from . import db
from datetime import datetime

class ExceptionTable(db.Model):
    __tablename__ = 'exception'
    objectid = db.Column(db.Integer, primary_key=True)
    exception_content = db.Column(db.Text)
    createdTime = db.Column(db.DateTime, default=datetime.now)