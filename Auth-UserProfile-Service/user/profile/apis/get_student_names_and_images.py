from flask_restx import Resource
from flask import request,jsonify

from user.profile.models.student import StudentModel
from user import api
import requests
import pandas as pd

from user.profile.apis.user_profile import profile

#this API will get a post request from "Newsfeed service" to get "student names" corresponding to "student ids"
@profile.route('/get_student_names_and_images')
class GetStudentNamesAndImages(Resource):
    @profile.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})
    def post(self):

        try: 

            student_ids = request.get_json()
            student_ids_pd=pd.DataFrame(student_ids)        
        
            #we got the "student_ids_pd" .now we will build a table of (student_id,student_names) using pandas
            student_names_with_ids = StudentModel.query.with_entities(StudentModel.id,StudentModel.username,StudentModel.profile_picture_link).all()
            student_names_with_ids_dicts =[]

            for student_name_with_id in student_names_with_ids:
                student_names_with_ids_dicts.append({"student_id":student_name_with_id.id,"username":student_name_with_id.username,"profile_picture_link":student_name_with_id.profile_picture_link})

            student_names_with_ids_pd = pd.DataFrame(student_names_with_ids_dicts)    

            #Now we wll join two panda table ...1)a table with one column of student ids 2)a table with columns (student_id,username)
            joined_pd = pd.merge(student_ids_pd, student_names_with_ids_pd, on='student_id', how='inner')
            joined_pd_dicts = joined_pd.to_dict(orient='records') #it converts a panda table to a array of dictionary
            # print(joined_pd_dicts)

            return jsonify(joined_pd_dicts)

            # response = requests.get(f'http://localhost:5000//beyond-the-seas.org/api/newsfeed/{user_id}/get_own_posts')
            # if response:
            #     return jsonify(response.json())
            # return {'message': 'student names not found'}, 404

        except Exception as e:
            print({"message":"exception occured in get_student_names"})
            print(e)
            return jsonify({"message":"exception occured in get_student_names"})

