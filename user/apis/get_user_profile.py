from flask_restx import Resource

from user.models.student import StudentModel

class GetUserProfile(Resource):
    def get(self, user_id):
        student = StudentModel.query.filter_by(id=user_id).first()
        if student:
            return student.json()
        return {'message': 'Student not found'}, 404
