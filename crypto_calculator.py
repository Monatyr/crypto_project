from datetime import datetime
import time
from api_functions import get_crypto_price

api_key_crypto = 'b247350e-d4f6-4bb1-8860-c6d7365311af'
api_url_base_crypto = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


def calc_zero_income_target(starting_price, fee = 0.025):
    return starting_price/(1-fee)

def periodicCheck(starting_price, crypto_name = "BTC", interval = 60):
    while True:
        start = datetime.now()
        
        curr_price = get_crypto_price(crypto_name, api_url_base_crypto, api_key_crypto)

        if(curr_price >= calc_zero_income_target(starting_price)):
            print("Gains")
        else:
            print("Losses")

        end = datetime.now()

        exec_time = end - start

        time.sleep(interval - exec_time.total_seconds())

periodicCheck(4600)