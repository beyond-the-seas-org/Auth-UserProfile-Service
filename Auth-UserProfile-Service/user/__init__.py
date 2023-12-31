from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2, dotenv, os
from flask_restx import Api, Namespace
from flask_cors import CORS
from flask import jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, get_jwt_identity,
    create_access_token, create_refresh_token
)


app = Flask(__name__)
api = Api(app)
CORS(app,origins = 'http://127.0.0.1:3000')


dotenv.load_dotenv()
db_url = os.getenv('DATABASE_URL')

conn = psycopg2.connect(db_url, sslmode='prefer')

# app.config['SQLALCHEMY_DATABASE_URI'] = db_url
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object('user.config.DevelopmentConfig')
db = SQLAlchemy(app)
blacklist = set()
jwt = JWTManager(app)


from user.profile.apis.user_profile import profile
from user.auth.apis.signup import auth
from user.auth.apis.login import auth
from user.auth.apis.logout import auth
from user.profile.apis.get_own_posts import profile
from user.profile.apis.get_student_names_and_images import profile
from user.profile.apis.create_dummy_user import profile
from user.profile.apis.get_cgpa_and_gre import profile
from user.profile.apis.add_to_shortlist import profile
from user.profile.apis.remove_from_shortlist import profile
from user.profile.apis.get_shortlisted_professors import profile
from user.profile.apis.get_student_info import profile
from user.profile.apis.get_ieee_publication_info import profile
from user.profile.apis.add_profile_picture import profile


api.add_namespace(profile)
api.add_namespace(auth)
