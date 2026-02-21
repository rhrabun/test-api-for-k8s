from flask import Flask, config
from flask_restful import Api
from .resources.status import Status


# Api initialization
app = Flask(__name__)
api = Api(app)

# Adding Api routes
api.add_resource(Status, '/', '/status')
