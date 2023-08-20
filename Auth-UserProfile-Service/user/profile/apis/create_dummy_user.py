from flask_restx import Resource, fields, Namespace
from sqlalchemy import func
from user import db, api
from flask import request

from user.profile.models.student import StudentModel
profile = Namespace('api/profile')


@profile.route('/create_dummy_user')
class CreateDummtUser(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def post(self):
        student = StudentModel()
        student.username = request.json['username']
        student.first_name = request.json['first_name']
        student.last_name = request.json['last_name']
        student.primary_email = request.json['primary_email']
        student.gender = "male"
        student.age = 25
        student.password_hash = request.json['password_hash']
        student.secondary_email = "abcd1234@gmail.com"
        student.bsc_year_of_passing = 2015
        student.ms_year_of_passing = 2017
        student.bsc_cgpa = request.json['bsc_cgpa']
        student.ms_cgpa = 3.90
        student.bsc_university = "BUET"
        student.ms_university = "BUET"
        student.github_link = request.json['github_link']
        student.linkedin_link = request.json['linkedin_link']
        student.website_link = request.json['website_link']
        student.current_address = "ABCD"
        student.gre_verbal_quant_score = 9
        student.gre_awa_score = request.json['gre_awa_score']
        student.toefl_score = 10
        student.ielts_score = 7

        db.session.add(student)
        db.session.commit()
        return student.json()
        
    
    