from . import db
from datetime import datetime

class IgnoreExceptionTable(db.Model):
    """
    记录忽略的异常
    """
    __tablename__ = 'ignore_exception'
    Id = db.Column(db.Integer, primary_key=True)
    exception_content = db.Column(db.Text)
    createdTime = db.Column(db.DateTime, default=datetime.now)


class ExceptionTable(db.Model):
    """
    记录异常
    """
    __tablename__ = 'exception'
    objectid = db.Column(db.Integer, primary_key=True)
    exception_content = db.Column(db.Text)
    createdTime = db.Column(db.DateTime, default=datetime.now)
    updatedTime = db.Column(db.DateTime, default=datetime.now)

