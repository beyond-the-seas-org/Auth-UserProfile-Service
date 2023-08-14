from flask_restx import Resource
from flask import request,jsonify

from user.profile.models.student import StudentModel
from user import api
import requests

from user.profile.apis.user_profile import profile

#this API will get a post request from "Newsfeed service" to get student names corresponding to "student ids"
@profile.route('//<int:user_id>/own_posts')
class GetOwnPosts(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def get(self, user_id):
        response = requests.get(f'http://localhost:5000//api/newsfeed/{user_id}/get_own_posts')
        if response:
            return jsonify(response.json())
        return {'message': 'own posts not found'}, 404

