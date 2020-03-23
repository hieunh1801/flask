from flask_restful import Api
from src.user.user_api import UserAPI, UserListAPI


api = Api()
api.add_resource(UserListAPI, "/api/users")
api.add_resource(UserAPI, "/api/users/<user_id>")
