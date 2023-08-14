from flask_restx import Resource, fields, Namespace
from flask import request

from user.profile.models.student import StudentModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from user.auth.apis.signup import auth
from user.profile.apis.user_profile import authorization_header
from user import jwt

blocklist = set()
@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(_,decrypted_token):
    jti = decrypted_token['jti']
    return jti in blocklist

@auth.route('/logout')
class Logout(Resource):
    @auth.doc(responses={200: 'OK', 400: 'Bad Request', 500: 'Internal Server Error'})
    @auth.expect(authorization_header)
    @jwt_required()
    def post(self):
        # implement the logout logic using the blacklist
        jti = get_jwt_identity()
        blocklist.add(jti)
        return {'message': 'Successfully logged out.'}, 200
    




