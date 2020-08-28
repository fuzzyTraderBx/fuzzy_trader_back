from flask_restful import Resource, reqparse

from models.investment import InvestmentModel
from flask_jwt_extended import jwt_required

from models.order import Order


class Investments(Resource):
    @jwt_required
    def get(self):
        args = reqparse.RequestParser()
        args.add_argument('user_id')
        total_investments = 0

        data = args.parse_args()
        orders = Order.find(data['user_id'])
        for item in orders:
            invest = InvestmentModel.find(item.investment_id)
            total_investments += invest.value
        return {
            'investments': len(orders),
            'total': total_investments
        }


    # Buy investment
    @jwt_required
    def post(self):

        args = reqparse.RequestParser()
        args.add_argument('user_id')
        args.add_argument('investment_id')

        data = args.parse_args()

        if InvestmentModel.find(data['investment_id']):
            print("Investment already registered on database")

        else:
            # Load with API data
            new_investment = InvestmentModel(data['investment_id'], 'abcd', 200, True)
            new_investment.save_investment()

        order = Order(data['user_id'], data['investment_id'])
        order.save_order()

        return {'message': 'Congrats! Your order have been saved!'}, 200