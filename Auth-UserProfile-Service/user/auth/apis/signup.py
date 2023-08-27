from flask_restx import Resource, fields, Namespace
from sqlalchemy import func
from user import db
from flask import request

from user.profile.models.student import StudentModel, signup_model
from werkzeug.security import generate_password_hash, check_password_hash

auth = Namespace('api/auth')

@auth.route('/signup')
class SignUp(Resource):
    @auth.doc(responses={201: 'Created', 400: 'Bad Request', 404: 'Not Found', 500: 'Internal Server Error'})
    @auth.expect(signup_model)
    def post(self):
        # parse the request body
        request_body = request.get_json()

        # list of expected fields in the request body
        expected_fields = ['username', 'first_name', 'last_name', 'primary_email', 'gender', 'age', 'password_hash']

        # check if all expected fields are present and not empty
        for field in expected_fields:
            if field not in request_body or not request_body[field]:
                return {'message': f'Missing or empty field: {field}'}, 400

        # create a new user profile
        new_user_profile = StudentModel(
            username=request_body['username'],
            first_name=request_body['first_name'],
            last_name=request_body['last_name'],
            primary_email=request_body['primary_email'],
            gender=request_body['gender'],
            age=request_body['age'],
            password_hash=generate_password_hash(request_body['password_hash'])
        )

        try:
        # add the new user profile to the database
            db.session.add(new_user_profile)
            db.session.commit()
        except:
            return {'message': 'User profile already exists! Try some other username.'}, 500
        return {'message': 'New user profile created successfully. Login now!'}, 201
