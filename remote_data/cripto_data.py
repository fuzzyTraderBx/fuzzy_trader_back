from bitcoinaverage import RestfulClient

from models.investment import InvestmentModel

public_key = 'YjUxZDI3MmE3ZmU3NDQwNWE4NmJjMGZjNjgzNTIyMDc'
secret_key = 'YTZmYzQ5MTRiMDYxNDFlZjhiNzAwYzA2NmQ1MmJmZTU2NmJjZTE2YmRjOTg0YzA3ODg4ZTAyZTAzYzZmMGEwZQ'

restful_client = RestfulClient(secret_key, public_key)
currencies = ['BTCUSD', 'ETHUSD', 'LTCUSD']  # Some currencies

def get_cripto(max_price):

    result = []

    for currency in currencies:
        ticker_global_per_symbol = restful_client.ticker_global_per_symbol(currency)
        price = ticker_global_per_symbol["last"]
        if price <= float(max_price):
            investment = InvestmentModel(currency, price, True)
            result.append(investment.json())
        print('Global Ticker for ' + currency)
        print(price)

    return result


def retrieve_investment(investment_key):
    if investment_key in currencies:
        investment = restful_client.ticker_global_per_symbol(investment_key)
        investment = InvestmentModel(investment_key, investment["last"], True)

        return investment

    return None
