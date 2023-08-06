from flask_restx import Resource
from flask import request,jsonify

from user.models.student import StudentModel
from user import api
import requests

class GetOwnPosts(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def get(self, user_id):
        # student = StudentModel.query.filter_by(id=user_id).first()
        # if student:
        #     return student.json()
        # return {'message': 'Student not found'}, 404
        response = requests.get(f'http://localhost:5000//beyond-the-seas.org/api/newsfeed/{user_id}/get_own_posts')
        if response:
            return jsonify(response.json())
        return {'message': 'own posts not found'}, 404

