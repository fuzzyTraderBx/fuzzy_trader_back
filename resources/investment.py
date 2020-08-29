from flask import jsonify
from flask_restful import Resource, reqparse

from models.investment import InvestmentModel
from flask_jwt_extended import jwt_required

from models.order import Order
from remote_data.cripto_data import get_cripto, retrieve_investment


class ListInvestments(Resource):
    @jwt_required
    def get(self, max_price):

        suitable_investments = get_cripto(max_price)
        return jsonify(suitable_investments)


class Investments(Resource):
    # Get all investments of a user
    @jwt_required
    def get(self, user_id):
        user_id = int(user_id)
        total_investments = 0

        investments = []

        orders = Order.find(user_id)
        for item in orders:
            invest = InvestmentModel.find_by_id(item.investment_id)
            investments.append(invest.json())
            total_investments += invest.value
        return {
            'investments': investments,
            'total': total_investments
        }


    # Buy investment
    @jwt_required
    def post(self, user_id):

        user_id = int(user_id)
        print(user_id)

        args = reqparse.RequestParser()
        args.add_argument('investment_key')

        data = args.parse_args()

        new_investment = InvestmentModel.find(data['investment_key'])
        if new_investment:
            print("Investment already registered on database")

        else:
            print("BUSCANDO INFORMACOES..........")
            # Load with API data
            new_investment = retrieve_investment(data['investment_key'])
            new_investment.save_investment()

        order = Order(user_id, new_investment.id)
        order.save_order()

        return {'message': 'Congrats! Your order have been saved!'}, 200
