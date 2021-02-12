from datetime import datetime
import time
import csv
from api_functions import get_crypto_price

api_key_crypto = 'b247350e-d4f6-4bb1-8860-c6d7365311af'
api_url_base_crypto = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

def calc_zero_income_target(starting_price, fee = 0.025):
    return starting_price/(1-fee)

def periodicCheck(starting_price, crypto_name = "BTC", interval = 60):

    zero_income_target = calc_zero_income_target(starting_price)
    timestamp = datetime.now()
    print(zero_income_target)

    while True:
        start = datetime.now()
        
        curr_price = round(get_crypto_price(crypto_name, api_url_base_crypto, api_key_crypto), 2)

        file = open('{}_data.csv'.format(crypto_name), 'a', newline = '')

        writer = csv.writer(file, delimiter = ',')

        writer.writerow([timestamp, curr_price])
        file.close()

        if(curr_price >= zero_income_target):
            print("Gains: +", curr_price - zero_income_target)
        else:
            print("Losses: ", curr_price - zero_income_target)

        end = datetime.now()

        exec_time = end - start

        break
        time.sleep(interval - exec_time.total_seconds())


def calc_plus_value(starting_price, amount, crypto_name = 'BTC', api_url_base_crypto = api_url_base_crypto, api_key_crypto = api_key_crypto):
    print(round((get_crypto_price(crypto_name, api_url_base_crypto, api_key_crypto) - calc_zero_income_target(starting_price))*amount/starting_price, 2))

periodicCheck(47073, 'BTC')
calc_plus_value(47073, 100)