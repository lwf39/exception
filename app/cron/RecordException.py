from app.db_table.exception_table import ExceptionTable
from  app.utils.get_etcd_data import get_etcd_data
from app.db_table import db
from app.models.Exception import get_all_ignore_exception
from flask_apscheduler import APScheduler
from app.utils.dingding import Ding_ding
from config import aliyun_url
scheduler = APScheduler()

# 查找exception项目中etcd库中前一分钟新增异常数据
@scheduler.task('interval', id='get_exception', seconds=60)
def get_exception_data():
    print('执行定时任务')
    data_exception = get_etcd_data()
    ignore_exception = [item["content"] for item in get_all_ignore_exception()]
    if len(data_exception) > 0:
        for exception in data_exception:
            for ingore in ignore_exception:
                if ingore in exception:
                    break
                else:
                    try:
                        exception_content = ExceptionTable.query.filter_by(exception_content=exception).first()
                        if not exception_content:
                            exception_content = ExceptionTable(exception_content=exception)
                            db.session.add(exception_content)
                            db.session.commit()
                            send_dingding(exception_content)
                    except Exception as e:
                        db.session.rollback()

def send_dingding(exceptioncontent):
    dingding = Ding_ding('SLS存在新的异常')
    url = f'<a href="{aliyun_url}" target="_blank">{exceptioncontent}</a>'
    
    dingding.ding_proxy(exceptioncontent)