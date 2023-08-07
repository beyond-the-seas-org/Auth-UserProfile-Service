from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2, dotenv, os
from flask_restx import Api, Namespace
from flask_cors import CORS
from flask_jwt_extended import JWTManager 

app = Flask(__name__)
api = Api(app)
CORS(app,origins = 'http://localhost:8000')


dotenv.load_dotenv()
db_url = os.getenv('DATABASE_URL')

conn = psycopg2.connect(db_url, sslmode='prefer')

# app.config['SQLALCHEMY_DATABASE_URI'] = db_url
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object('user.config.DevelopmentConfig')
db = SQLAlchemy(app)
jwt = JWTManager(app)


from user.profile.apis.update_user_profile import profile
from user.auth.apis.signup import auth
from user.profile.apis.get_user_profile import profile

api.add_namespace(profile)
api.add_namespace(auth)