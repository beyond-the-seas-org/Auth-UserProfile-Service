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
    'gender': fields.String,
    'age': fields.Integer,
})


# create user profiles
class CreateUserProfiles(Resource):
    # @api.doc(responses={201: 'Created', 400: 'Bad Request', 500: 'Internal Server Error'})
    @api.expect(resource_fields)
    def post(self):
        max_id = db.session.query(func.max(StudentModel.id)).scalar()
        if (max_id == 'None'):
            max_id = 1
        else:
            max_id = max_id + 1
        
        # parse the request body
        request_body = request.get_json()
        # create a new user profile
        new_user_profile = StudentModel()
        new_user_profile.id = max_id
        new_user_profile.username = request_body['username']
        new_user_profile.first_name = request_body['first_name']
        new_user_profile.last_name = request_body['last_name']
        new_user_profile.primary_email = request_body['primary_email']
        new_user_profile.gender = request_body['gender']
        new_user_profile.age = request_body['age']
        
        # add the new user profile to the database
        db.session.add(new_user_profile)
        db.session.commit()

        return {'message': 'New user profile created successfully.'}, 201
