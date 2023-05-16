user = 'root'
password = '123456'
host = '127.0.0.1'
database = 'exception'
SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s:3306/%s" % (user, password, host,database)
# SQLALCHEMY_ECHO = True