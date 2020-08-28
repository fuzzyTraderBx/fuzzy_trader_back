from flask_restful import Resource, reqparse

from models.investment import InvestmentModel
from flask_jwt_extended import jwt_required


class Investments(Resource):
    def get(self):
        return {'investments': []}

    # Buy investment
    @jwt_required
    def post(self):

        args = reqparse.RequestParser()
        args.add_argument('user_id')
        args.add_argument('investment_id')

        data = args.parse_args()

        if InvestmentModel.find(data['investment_id']):
            return {'message': 'Already in database: creating user_investment'}, 400

        # Load with API data
        new_investment = InvestmentModel(data['investment_id'], 'abcd', 200, True)
        new_investment.save_investment()
        return new_investment.json()