from app.db_table.exception_table import IgnoreExceptionTable, ExceptionTable
from app.db_table import db

def get_all_ignore_exception(page,size):
    result = IgnoreExceptionTable.query.paginate(page=page, per_page=size, error_out=False)
    total = result.total
    data = [{"content": exception_data.exception_content} for exception_data in result.items]
    data = {"total": total, "data": data}
    return data

def del_ignore_exception(content):
    try:
        exception_content = IgnoreExceptionTable.query.filter_by(exception_content=content).first()
        db.session.delete(exception_content)
        db.session.commit()
    except Exception as e:
        raise RuntimeError("删除失败")


def add_ignore_exception(content,modify_data):
    try:
        print(content,modify_data)
        exception_content = IgnoreExceptionTable.query.filter_by(exception_content=content).first()
        print(exception_content)
        if exception_content:
            exception_content.exception_content = modify_data
        else:
            exception_content = IgnoreExceptionTable(exception_content=modify_data)
            db.session.add(exception_content)
        db.session.commit()
        return 200
    except Exception as e:
        return 404
    
def add_exception(content):
    try:
        exception_content = ExceptionTable.query.filter_by(exception_content=content).first()
        print(exception_content)
        if not exception_content:
            exception_content = ExceptionTable(exception_content=content)
            db.session.add(exception_content)
        db.session.commit()
        return 200
    except Exception as e:
        return 404