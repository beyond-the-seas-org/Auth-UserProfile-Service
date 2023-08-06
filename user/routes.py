from user.apis.get_user_profile import GetUserProfile
from flask_restx import Api
from user import app

api = Api(app)

profile = api.namespace('api/user')
profile.add_resource(GetUserProfile, '/<int:user_id>/profile')