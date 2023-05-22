user = 'root'
password = '123456'
host = '127.0.0.1'
database = 'exception'
SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s:3306/%s" % (user, password, host,database)
# SQLALCHEMY_ECHO = True
# headers = { 'Content-Type': 'application/json', 'charset': 'utf-8' }
# etcd_host exception-mining 项目的etcd地址
etcd_host = '10.1.186.210'
aliyun_url = 'https://sls.console.aliyun.com/lognext/project/dth3yunproject/logsearch/dth3yunprojectstore'