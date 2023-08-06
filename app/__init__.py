from flask import Flask,request,jsonify
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app)

app.config.from_object('app.config.DevelopmentConfig')

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}