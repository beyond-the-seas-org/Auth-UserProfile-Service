from flask_restx import Resource
from flask import request,jsonify

from user.profile.models.student import StudentModel
from user import api

from user.profile.apis.user_profile import profile

@profile.route('/<int:user_id>/get_cgpa_and_gre')
class GetCgpaAndGreScrore(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def get(self, user_id):

        try:
            student = StudentModel.query.get(user_id)
            cgpa_and_gre = {}
            cgpa_and_gre['cgpa'] = student.ms_cgpa
            cgpa_and_gre['gre_verbal_quant_score'] = student.gre_verbal_quant_score
            cgpa_and_gre['gre_awa_score'] = student.gre_awa_score
            return jsonify(cgpa_and_gre)
        
        except Exception as e:
            print({"message":"exception occured in get_cgpa_and_gre"})
            print(e)
            return jsonify({"message":"exception occured in get_cgpa_and_gre"})





       
