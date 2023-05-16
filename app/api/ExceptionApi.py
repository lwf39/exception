from flask_restful import reqparse, Resource


class ExceptionTableApi(Resource):
    def get(self):
        return {'hello': 'world'}
    
    def delete(self):
        pass

    def post(self):
        pass