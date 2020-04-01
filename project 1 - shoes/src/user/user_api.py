from flask_restful import Resource
from flask import jsonify
from .user_model import User, UserSchema


class UserListAPI(Resource):
    def get(self):
        total = User.query.paginate(1, 2).total  # get total
        pages = User.query.paginate(1, 2).pages  # get total page
        users = User.query.paginate(
            page=1, per_page=2).items  # get item for page
        data = UserSchema().dump(users, many=True)
        print(data)
        return jsonify(data)

    def post(self):
        return "Post API"


class UserAPI(Resource):
    def get(self, user_id):
        return "UserListAPI GET " + user_id

    def put(self, user_id):
        return "UserListAPI PUT " + user_id

    def delete(self, user_id):
        return "UserListAPI DELETE " + user_id
