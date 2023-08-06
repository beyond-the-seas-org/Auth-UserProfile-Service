from user.apis.get_user_profile import *
from user.apis.create_user_profile import *
from user.apis.update_user_profile import *

profile = api.namespace('api/user')
profile.add_resource(GetUserProfile, '/<int:user_id>/profile')
profile.add_resource(CreateUserProfiles, '/create')
profile.add_resource(UpdateUserProfiles, '/<int:user_id>/update')