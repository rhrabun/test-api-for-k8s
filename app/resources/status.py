import socket

from flask_restful import Resource


class Status(Resource):
    def get(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return {'status': 'Api is working',
                'hostname': f'{hostname}',
                'ip': f'{ip}',
                'apiVersion': '2'}, 200
