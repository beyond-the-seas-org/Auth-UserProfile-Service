from flask_restx import Resource, fields, Namespace
from sqlalchemy import func
from user import db, api
from flask import request,jsonify

from user.profile.apis.user_profile import profile
from user.profile.models.shortlist import ShortlistModel

from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError

@api.errorhandler(NoAuthorizationError)
def handle_auth_required(e):
    return {"message": "Authorization token is missing"}, 401



#this API will remove an entry for a student who remove a  professor from shorlist
@profile.route('/remove_from_shortlist')
class RemoveFromShortlist(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    @jwt_required()
    def post(self):

        try:
        
            #get the student_id and professor_id from the request
            student_id = request.json['student_id']
            professor_id = request.json['professor_id']
            #delete the entry from the shortlist
            shortlist_entry = ShortlistModel.query.filter_by(student_id=student_id,professor_id=professor_id).first()
            db.session.delete(shortlist_entry)
            db.session.commit()
     
            return jsonify({'message': 'deleted from shortlist'})
    
        except Exception as e:
            print({'message': 'error occured in deleted_from_shortlist'})
            print(e)
            return jsonify({'message': 'error occured in deleted_from_shortlist'})

