from flask_restx import Resource, fields, Namespace
from flask import request

from user.profile.models.student import StudentModel
from flask_jwt_extended import jwt_required, get_jwt
from user.auth.apis.signup import auth
from user.profile.apis.user_profile import authorization_header
from user import jwt
from user import blacklist


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist

@auth.route('/logout')
class Logout(Resource):
    @auth.doc(responses={200: 'OK', 400: 'Bad Request', 500: 'Internal Server Error'})
    @auth.expect(authorization_header)
    @jwt_required()
    def post(self):
        # implement the logout logic using the blacklist
        jti = get_jwt()['jti']
        blacklist.add(jti)
        return {'message': 'Successfully logged out.'}, 200
    




