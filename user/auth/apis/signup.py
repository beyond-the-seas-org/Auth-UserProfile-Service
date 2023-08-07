from flask_restx import Resource, fields, Namespace
from sqlalchemy import func
from user import db
from flask import request

from user.profile.models.student import StudentModel, signup_model

from werkzeug.security import generate_password_hash, check_password_hash


auth = Namespace('api/auth')

@auth.route('/signup')
class SignUp(Resource):
    @auth.doc(responses={201: 'Created', 400: 'Bad Request', 500: 'Internal Server Error'})
    @auth.expect(signup_model)
    @auth.marshal_with(signup_model)
    def post(self):
        # parse the request body
        request_body = request.get_json()
        # create a new user profile

        new_user_profile = StudentModel(
            username = request_body['username'],
            first_name = request_body['first_name'],
            last_name = request_body['last_name'],
            primary_email = request_body['primary_email'],
            gender = request_body['gender'],
            age = request_body['age'],
            password_hash = generate_password_hash(request_body['password_hash'])
        )
    
        # add the new user profile to the database
        db.session.add(new_user_profile)
        db.session.commit()

        return {'message': 'New user profile created successfully.'}, 201
