from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.investment import Investments, ListInvestments
from resources.user import Users, UserLogin, UserLogout
from blockedlist import BLOCKEDLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # TODO: hide this
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def create_database():
    database.create_all()


@jwt.token_in_blacklist_loader
def verify_blockedlist(token):
    return token['jti'] in BLOCKEDLIST


@jwt.revoked_token_loader
def invalid_access_token():
    return jsonify({'message': 'You have been logged out'}), 401


api.add_resource(Investments, '/investments/<user_id>')

api.add_resource(Users, '/signup')

api.add_resource(UserLogin, '/login')

api.add_resource(UserLogout, '/logout')

api.add_resource(ListInvestments, '/list_investments/<max_price>')

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)
