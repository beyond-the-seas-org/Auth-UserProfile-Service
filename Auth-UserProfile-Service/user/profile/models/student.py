from user import db
from flask_restx import fields, Model
from user import api

login_model = api.model('login_model', {
    'username': fields.String(required=True),
    'password_hash': fields.String(required=True)
})

signup_model = api.clone('signup_model', login_model,{
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'primary_email': fields.String(required=True),
    'gender': fields.String(required=True),
    'age': fields.Integer(required=True)
})

update_model = api.clone('update_model', signup_model, {
    'bsc_year_of_passing': fields.Integer,
    'ms_year_of_passing': fields.Integer,
    'bsc_cgpa': fields.Float,
    'ms_cgpa': fields.Float,
    'bsc_university': fields.String,
    'ms_university': fields.String,
    'github_link': fields.String,
    'linkedin_link': fields.String,
    'website_link': fields.String,
    'current_address': fields.String,
    'gre_verbal_quant_score': fields.Integer,
    'gre_awa_score': fields.Float,
    'toefl_score': fields.Integer,
    'ielts_score': fields.Float
})



# Create a model for the table 'student'
class StudentModel(db.Model):
    """
    primary key: student_id
    foreign key: publication_id
    other fields: username, password_hash, first_name, last_name, primary_email, secondary_email, bsc_year_of_passing, gender,
    age, msc_year_of_passing, bsc_cgpa, msc_cgpa,
    bsc_university, msc_university, github_link, linkedin_link,
    website_link, current_address
    """

    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # publication_id = db.Column(db.Integer, db.ForeignKey('publications.publication_id'))

    # mandatory fields
    username = db.Column(db.String(500), nullable=False, unique=True)
    password_hash = db.Column(db.String(500), nullable=False, unique=True)
    first_name = db.Column(db.String(500), nullable=False)
    last_name = db.Column(db.String(500), nullable=False)
    primary_email = db.Column(db.String(500), nullable=False, unique=True)
    gender = db.Column(db.String(500), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # optional fields
    secondary_email = db.Column(db.String(500))
    bsc_year_of_passing = db.Column(db.Integer)
    ms_year_of_passing = db.Column(db.Integer)
    bsc_cgpa = db.Column(db.Float)
    ms_cgpa = db.Column(db.Float)
    bsc_university = db.Column(db.String(500))
    ms_university = db.Column(db.String(500))
    github_link = db.Column(db.String(500), unique=True)
    linkedin_link = db.Column(db.String(500), unique=True)
    website_link = db.Column(db.String(500), unique=True)
    current_address = db.Column(db.String(1000))
    gre_verbal_quant_score = db.Column(db.Integer)
    gre_awa_score = db.Column(db.Float)
    toefl_score = db.Column(db.Integer)
    ielts_score = db.Column(db.Float)
    profile_picture_link = db.Column(db.String(1000))

    
    # create a json method
    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'primary_email': self.primary_email,
            'secondary_email': self.secondary_email,
            'gender': self.gender,
            'age': self.age,
            'password_hash': self.password_hash,
            'bsc_year_of_passing': self.bsc_year_of_passing,
            'ms_year_of_passing': self.ms_year_of_passing,
            'bsc_cgpa': self.bsc_cgpa,
            'ms_cgpa': self.ms_cgpa,
            'bsc_university': self.bsc_university,
            'ms_university': self.ms_university,
            'github_link': self.github_link,
            'linkedin_link': self.linkedin_link,
            'website_link': self.website_link,
            'current_address': self.current_address,
            'gre_verbal_quant_score': self.gre_verbal_quant_score,
            'gre_awa_score': self.gre_awa_score,
            'toefl_score': self.toefl_score,
            'ielts_score': self.ielts_score,
            'profile_picture_link': self.profile_picture_link
        }