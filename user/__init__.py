from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2, dotenv, os

app = Flask(__name__)

dotenv.load_dotenv()
db_url = os.getenv('DATABASE_URL')

conn = psycopg2.connect(db_url, sslmode='prefer')

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from user.routes import api