from flask_restful import Resource

wallet = {
    'total': 800,
    'investments': [
        {
            'investment_id': '1234',
            'investment_name': 'investment X',
            'investment_value': '$500',
            'is_criptocurrency': True,
        },
        {
            'investment_id': '5678',
            'investment_name': 'investment Y',
            'investment_value': '$600',
            'is_criptocurrency': False,
        }
    ]
}


class Wallet(Resource):
    def get(self):
        return {'wallet': wallet}