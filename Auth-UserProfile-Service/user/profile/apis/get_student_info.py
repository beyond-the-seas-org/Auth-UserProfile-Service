from flask_restx import Resource
from flask import request,jsonify
from user import api

from user.profile.apis.user_profile import profile
from user.profile.models.student import StudentModel


@profile.route('/<int:user_id>/get_student_info')
class GetStudentInfo(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def get(self, user_id):

        try:
            student = StudentModel.query.get(user_id)
           
            return jsonify(student.json())
        
        except Exception as e:
            print({"message":"exception occured in get_cgpa_and_gre"})
            print(e)
            return jsonify({"message":"exception occured in get_cgpa_and_gre"})





       
