import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='username cannot be converted'
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='password cannot be converted'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "the username has been used, try the new one"}, 400
        print(data)
        new_user = UserModel(name=data['username'], password=data['password'])

        new_user.save_in_db()
        return {"message": "User created successfully."}, 201
