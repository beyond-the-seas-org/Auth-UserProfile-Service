from flask_restx import Resource, fields, Namespace
from flask import request

from user.profile.models.student import StudentModel, login_model
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, create_refresh_token, jwt_required
from user.auth.apis.signup import auth


@auth.route('/login')
class Login(Resource):

    @auth.doc(responses={200: 'OK', 400: 'Bad Request', 500: 'Internal Server Error'})
    @auth.expect(login_model)
    def post(self):
        request_body = request.get_json()
        # check if request body is complete or not
        if request_body['username'] == '' or request_body['password_hash'] == '':
            return {'message': 'Missing fields!'}, 400

        # check if the user profile exists
        student = StudentModel.query.filter_by(username=request_body['username']).first()
        if student:
            # check if the password is correct
            if check_password_hash(student.password_hash, request_body['password_hash']):
                # generate the access token
                access_token = create_access_token(identity=student.id)
                refresh_token = create_refresh_token(identity=student.id)
                return {'id': student.id, 'access_token': access_token, 
                        'refresh_token': refresh_token}, 200
            return {'message': 'Incorrect password.'}, 404
        return {'message': 'User profile not found.'}, 404
    

@auth.route('/refresh')
class Refresh(Resource):
    @auth.doc(responses={200: 'OK', 400: 'Bad Request', 500: 'Internal Server Error'})
    @jwt_required(refresh=True)
    def post(self):
        username = get_jwt_identity()
        student = StudentModel.query.filter_by(username=username).first()
        # generate the access token
        access_token = create_access_token(identity=student.id)
        return {'access_token': access_token}, 200
    
