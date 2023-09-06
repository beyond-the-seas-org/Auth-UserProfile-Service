from flask_restx import Resource
from flask import request,jsonify
from user import api
import requests

from user.profile.apis.user_profile import profile
from user.profile.models.shortlist import ShortlistModel

#this API will get "GET" request from "professor service" and will return "shortlisted_professors_ids" corresponding to "student id"
@profile.route('/<int:user_id>/get_shortlisted_professors')
class GetShortlistedProfessors(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def get(self, user_id):

        try:

            shortlisted_professors = ShortlistModel.query.filter_by(student_id=user_id).all()
            #print(shortlisted_professors)

            shortlisted_professors_ids = []
            if shortlisted_professors:
                shortlisted_professors_ids = [professor.professor_id for professor in shortlisted_professors]
            #print(shortlisted_professors) 
            
            return jsonify({'shortlisted_professors_ids': shortlisted_professors_ids })
        
        except Exception as e:
            print({"message":"exception occured in get_shortlisted_professors"})
            print(e)
            return jsonify({"message":"exception occured in get_shortlisted_professors"})
        
        

