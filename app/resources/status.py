from flask_restful import Resource


class Status(Resource):
    def get(self):
        return {'status': 'Api is working',
                'apiVersion': '1'}, 200
