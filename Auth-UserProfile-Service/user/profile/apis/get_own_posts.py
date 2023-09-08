from flask_restx import Resource
from flask import request,jsonify
from user import api
import requests

from user.profile.models.student import StudentModel
from user.profile.apis.user_profile import profile

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401


#this API will get a post request from "Newsfeed service" to get student names corresponding to "student ids"
@profile.route('//<int:user_id>/own_posts')
class GetOwnPosts(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def get(self, user_id):

        try:

            response = requests.get(f'http://127.0.0.1:5000//api/newsfeed/{user_id}/get_own_posts')
            if response:
                return jsonify(response.json())
            return jsonify({'message': 'own posts not found'})
        
        except Exception as e:
            print({"message":"exception occured in get_own_posts"})
            print(e)
            return jsonify({"message":"exception occured in get_own_posts"})

