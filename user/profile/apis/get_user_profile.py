from flask_restx import Resource, Namespace

from user.profile.models.student import StudentModel
from user.profile.apis.update_user_profile import profile


@profile.route('/<int:user_id>')
class GetUserProfile(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def get(self, user_id):
        student = StudentModel.query.filter_by(id=user_id).first()
        if student:
            return student.json()
        return {'message': 'Student not found'}, 404
