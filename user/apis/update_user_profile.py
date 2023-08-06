from flask_restx import Resource, fields
from sqlalchemy import func
from user import db
from flask import request

from user.models.student import StudentModel
from user import api

resource_fields = api.model('Student', {
    'username': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'primary_email': fields.String,
    'secondary_email': fields.String,
    'gender': fields.String,
    'age': fields.Integer,
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

# update user profiles
class UpdateUserProfiles(Resource):
    # @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @api.expect(resource_fields)
    def put(self, user_id):
        # parse the request body
        request_body = request.get_json()
        # check if the user profile exists
        student = StudentModel.query.filter_by(id=user_id).first()
        if student:
            # update the user profile
            student.username = request_body['username']
            student.first_name = request_body['first_name']
            student.last_name = request_body['last_name']
            student.primary_email = request_body['primary_email']
            student.gender = request_body['gender']
            student.age = request_body['age']

            student.secondary_email = request_body['secondary_email']
            student.bsc_year_of_passing = request_body['bsc_year_of_passing']
            student.ms_year_of_passing = request_body['ms_year_of_passing']
            student.bsc_cgpa = request_body['bsc_cgpa']
            student.ms_cgpa = request_body['ms_cgpa']
            student.bsc_university = request_body['bsc_university']
            student.ms_university = request_body['ms_university']
            student.github_link = request_body['github_link']
            student.linkedin_link = request_body['linkedin_link']
            student.website_link = request_body['website_link']
            student.current_address = request_body['current_address']
            student.gre_verbal_quant_score = request_body['gre_verbal_quant_score']
            student.gre_awa_score = request_body['gre_awa_score']
            student.toefl_score = request_body['toefl_score']
            student.ielts_score = request_body['ielts_score']

            # commit the changes to the database
            db.session.commit()
            return {'message': 'User profile updated successfully.'}, 200
        
        return {'message': 'User profile not found.'}, 404
    