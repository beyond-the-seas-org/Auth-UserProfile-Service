from flask_restx import Resource, fields, Namespace
from sqlalchemy import func
from user import db, api
from flask import request,jsonify

from user.profile.apis.user_profile import profile
from user.profile.models.shortlist import ShortlistModel


#this API will add an entry for a student who shorlists a professor
@profile.route('/add_to_shortlist')
class AddToShortlist(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def post(self):

        try:
        
            #get the student_id and professor_id from the request
            shortlist_entry = ShortlistModel()
            shortlist_entry.student_id = request.json['student_id']
            shortlist_entry.professor_id = request.json['professor_id']
            db.session.add(shortlist_entry)
            db.session.commit()
     
            return jsonify({'message': 'added on shortlist'})
    
        except Exception as e:
            print({'message': 'error occured in adding_to_shortlist'})
            print(e)
            return jsonify({'message': 'error occured in adding to shortlist'})

