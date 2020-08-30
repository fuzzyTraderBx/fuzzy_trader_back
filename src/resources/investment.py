from flask import jsonify
from flask_restful import Resource, reqparse

from src.models.investment import InvestmentModel
from flask_jwt_extended import jwt_required

from src.models.order import Order
from src.remote_data.cripto_data import get_cripto, retrieve_investment


class ListInvestments(Resource):
    @jwt_required
    def get(self, max_price):

        """
        Search investments by a defined max price
        :param max_price: specifies a max price
        :return: a list of suitable investments
        """

        suitable_investments = get_cripto(max_price)
        return jsonify(suitable_investments)


class Investments(Resource):
    @jwt_required
    def get(self, user_id):

        """
        Get all investments of a user
        :param user_id: id that specifies a buyer
        :return: return user's wallet that contains the total investment and a list of investments as a dict
        """

        user_id = int(user_id)
        total_investments = 0

        investments = []

        orders = Order.find(user_id)
        for item in orders:
            invest = InvestmentModel.find_by_id(item.investment_id)
            investments.append(invest.json())
            total_investments += invest.value

        investments_dict = {}

        for invest in investments:
            if invest['name'] in investments_dict:
                investments_dict[invest['name']]['quantity'] += 1
            else:
                investments_dict[invest['name']] = {}
                investments_dict[invest['name']]['quantity'] = 1
                investments_dict[invest['name']]['price'] = invest['value']

        return {
            'total': total_investments,
            'investments': investments_dict,
        }

    @jwt_required
    def post(self, user_id):

        """
        Buy a investment
        :param user_id: id that specifies a buyer
        :param_body investment_key that specifies the name of the investment
        :return: returns success if the order have been successful
        """

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
            if new_investment:
                new_investment.save_investment()
            else:
                return {'message': 'Investment not found. Verify your key.'}, 204

        order = Order(user_id, new_investment.id)
        order.save_order()

        return {'message': 'Congrats! Your order have been saved!'}, 200
