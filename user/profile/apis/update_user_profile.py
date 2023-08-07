from flask_restx import Resource, fields, Namespace
from sqlalchemy import func
from user import db
from flask import request

from user.profile.models.student import StudentModel, update_model
from werkzeug.security import generate_password_hash, check_password_hash

profile = Namespace('api/profile')


@profile.route('/<int:user_id>/update')
class UpdateUserProfiles(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @profile.expect(update_model)
    @profile.marshal_with(update_model)
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
            student.password_hash = generate_password_hash(request_body['password_hash'])
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
    