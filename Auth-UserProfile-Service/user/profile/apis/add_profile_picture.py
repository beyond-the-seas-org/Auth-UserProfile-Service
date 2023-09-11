from flask import Flask,request,jsonify
from flask_restx import Resource
from sqlalchemy import func
from user import db
from user import api
from user.profile.apis.user_profile import profile
import os


import boto3
import datetime

from user.profile.models.student import StudentModel

@profile.route('/add_profile_picture/<int:user_id>')
class Add_image(Resource):
    @api.doc(responses={200: 'OK', 404: 'Not Found', 500: 'Internal Server Error'})

    def put(self,user_id):

        try:

            student = StudentModel.query.get(user_id)
            image_file = request.files['image_file']

            # load the access keys from the env file using dotenv
            from dotenv import load_dotenv
            load_dotenv()

            ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
            SECRET_KEY = os.getenv('AWS_SECRET_KEY')
            BUCKET_NAME = 'beyond-the-seas-storage'

            s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

            image_file = request.files['image_file']
            filename = "profile_picture_"+str(user_id) + "." + image_file.filename.split('.')[-1]  # e.g., "uniquefilename.jpg"
            s3_client.upload_fileobj(image_file, BUCKET_NAME, filename,ExtraArgs={'ACL': 'public-read'})
            url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
           

            #insering the image url for the post into database
            student.profile_picture_link = url
            db.session.commit()
            
            return jsonify({'url': url, 'status': 'ok'})

        except Exception as e:
            print({"message":"exception occured in add_profile_picture"})
            print(e)
            return jsonify({"message":"exception occured in add_profile_picture"})

