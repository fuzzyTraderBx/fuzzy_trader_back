from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from blockedlist import BLOCKEDLIST

from models.user import UserModel

args = reqparse.RequestParser()
args.add_argument('name', type=str)
args.add_argument('email', type=str, required=True, help="Required Field!")
args.add_argument('password', type=str, required=True, help="Required Field!")


class Users(Resource):
    # Signup
    def post(self):

        data = args.parse_args()

        if UserModel.find(data['email']):
            return {"message": "The email '{}' already exists.".format(data['email'])}, 400


        # Load with API data
        new_user = UserModel(**data)
        new_user.save_user()
        return new_user.json(), 200


class UserLogin(Resource):

    @classmethod
    def post(cls):
        data = args.parse_args()

        user = UserModel.find(data['email'])
        print(user)
        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token, 'user': {'id': user.id}}, 200
        elif user:
            return {'message': "Invalid password"}, 204
        return {"message": "Invalid email or password."}, 206


class UserLogout(Resource):

    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']  # JWT Token Identifier
        BLOCKEDLIST.add(jwt_id)
        return {'message': 'Logged out successfully!'}, 200


