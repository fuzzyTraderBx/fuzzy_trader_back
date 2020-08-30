import datetime

import requests
from bitcoinaverage import RestfulClient

from models.investment import InvestmentModel
from variables import PUBLIC_KEY, SECRET_KEY, MARKET_ACCESS_KEY

public_key = PUBLIC_KEY
secret_key = SECRET_KEY

market_stack_url = 'http://api.marketstack.com/v1/tickers/'

restful_client = RestfulClient(secret_key, public_key)
currencies = ['BTCUSD', 'ETHUSD', 'LTCUSD']  # Some currencies
# stocks = ['MSFT', 'AAPL', 'AMZN', 'GOOG', 'GOOGL', 'FB', 'VOD', 'INTC', 'CMCSA', 'PEP', 'ADBE', 'CSCO', 'NVDA', 'NFLX',
#           'TSLA', 'COST', 'PYPL', 'AMGN', 'SNY', 'ASML']

stocks = ['MSFT']

def get_cripto(max_price):
    params = {
        'access_key': MARKET_ACCESS_KEY,
    }

    result = []

    for currency in currencies:
        ticker_global_per_symbol = restful_client.ticker_global_per_symbol(currency)
        price = ticker_global_per_symbol["last"]
        if price <= float(max_price):
            investment = InvestmentModel(currency, price, True)
            result.append(investment.json())
        print('Global Ticker for ' + currency)
        print(price)

    for stock in stocks:
        response = requests.get(market_stack_url + stock + '/eod', params=params)
        if response.status_code != 400:
            response = response.json()
            response = response['data']
            stock_historical = response['eod']
            price = stock_historical[0]['close']
            print(response['symbol'])
            if price <= float(max_price):
                if stock_historical:
                    investment = InvestmentModel(response['symbol'], price, False)
                    result.append(investment.json())
    return result


def retrieve_investment(investment_key):

    """
    I need to search into the api of actions a action "investment_key"
    :param investment_key:
    :return:
    """

    if investment_key in currencies:
        investment = restful_client.ticker_global_per_symbol(investment_key)
        investment = InvestmentModel(investment_key, investment["last"], True)

        return investment
    elif investment_key in stocks:
        # Searching data from stock api

        params = {
            'access_key': MARKET_ACCESS_KEY,
        }

        response = requests.get(market_stack_url + investment_key + '/eod', params=params)
        if response.status_code != 400:
            response = response.json()
            response = response['data']
            last_days = response['eod']
            print(response['symbol'])
            if last_days:
                investment = InvestmentModel(response['symbol'], last_days[0]['close'], False)

                return investment

    return None
