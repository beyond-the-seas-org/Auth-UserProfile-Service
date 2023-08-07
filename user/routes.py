from user.apis.get_user_profile import *
from user.apis.create_user_profile import *
from user.apis.update_user_profile import *
from user.apis.get_own_posts import *
from user.apis.get_student_names import *


profile = api.namespace('api/user')
profile.add_resource(GetUserProfile, '/<int:user_id>/profile')
profile.add_resource(CreateUserProfiles, '/create')
profile.add_resource(UpdateUserProfiles, '/<int:user_id>/update')
profile.add_resource(GetOwnPosts, '/<int:user_id>/own_posts')
profile.add_resource(GetStudentNames, '/get_student_names') ##this API req will come from "newsfeed service"