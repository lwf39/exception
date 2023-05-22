from app.db_table.exception_table import ExceptionTable
from  app.utils.get_etcd_data import get_etcd_data
from app.db_table import db
from app.db_table.exception_table import IgnoreExceptionTable
from flask_apscheduler import APScheduler
from app.utils.dingding import Ding_ding
from config import aliyun_url
scheduler = APScheduler()

# 查找exception项目中etcd库中前一分钟新增异常数据
@scheduler.task('interval', id='get_exception', seconds=60)
def get_exception_data():
    print('start cronjob')
    data_exception = get_etcd_data()
    with scheduler.app.app_context():
        ignore_exception = [item.exception_content for item in IgnoreExceptionTable.query.all()]
    print(f'新增异常:{data_exception}')
    if len(data_exception) > 0:
        for exception in data_exception:
            if check_ignore_exception(exception,ignore_exception):
                try:
                    with scheduler.app.app_context():
                        exception_content = ExceptionTable.query.filter_by(exception_content=exception).first()
                        if not exception_content:
                            print(f'发送新增告警:{exception}')
                            exception_content = ExceptionTable(exception_content=exception)
                            db.session.add(exception_content)
                            db.session.commit()
                            send_dingding(exception)
                except Exception as e:
                    db.session.rollback()

def check_ignore_exception(exception,ignore_exception):
    for i in ignore_exception:
        if i in exception:
            return False
    return True

def send_dingding(exceptioncontent):
    dingding = Ding_ding('SLS存在新的异常')
    url = f'<a href="{aliyun_url}" target="_blank">{exceptioncontent}</a>'
    dingding.ding_proxy(url)