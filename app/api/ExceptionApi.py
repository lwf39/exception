from flask_restful import reqparse, Resource
from app.models.Exception import get_all_ignore_exception, del_ignore_exception, add_ignore_exception
from flask import jsonify

class ExceptionModifyApi(Resource):
    """
    操作忽略异常表
    """
    def post(self):
        """
        添加和修改忽略的异常
        """
        parser = reqparse.RequestParser()
        parser.add_argument('content', type=str)
        parser.add_argument('old_content', type=str)
        args = parser.parse_args()
        res = add_ignore_exception(args['old_content'],args['content'])
        if res == 209:
            return {"message":"该内容已添加"}, 500
        elif res == 200:
            return {"message":"添加成功"}, 200

class ExceptionListApi(Resource):
    """
    操作忽略异常表
    """    
    def post(self):
        """
        添加和修改忽略的异常
        """
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('size', type=int)
        args = parser.parse_args()
        print(args['page'], args['size'])
        data = get_all_ignore_exception(args['page'], args['size'])
        return jsonify({'message': data})

class ExceptionTableApi(Resource):
    """
    操作忽略异常表
    """
    def post(self):
        """删除异常"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("content", type=str, required=True)
            args = parser.parse_args()
            exception_name = args["content"]
            del_ignore_exception(exception_name)
            return {"message":"删除成功"}, 200
        except Exception as e:
            return {"message":"删除失败"}, 500