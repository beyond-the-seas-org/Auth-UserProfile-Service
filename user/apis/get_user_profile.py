from flask_restx import Resource

from user.models.student import StudentModel
from user import api

class GetUserProfile(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def get(self, user_id):
        student = StudentModel.query.filter_by(id=user_id).first()
        if student:
            return student.json()
        return {'message': 'Student not found'}, 404
