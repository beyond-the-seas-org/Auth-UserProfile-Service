from flask_restx import Resource
from flask import request,jsonify

from user.models.student import StudentModel
from user import api
import requests

#this API will get a post request from "Newsfeed service" to get student names corresponding to "student ids"
class GetOwnPosts(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def post(self, user_id):
        response = requests.get(f'http://localhost:5000//api/newsfeed/{user_id}/get_own_posts')
        if response:
            return jsonify(response.json())
        return {'message': 'own posts not found'}, 404

