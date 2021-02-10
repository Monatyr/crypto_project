import json
import requests
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

api_key = 'f8804b422d57d97b61d0509ce7bd6537'
api_url_base = 'http://data.fixer.io/api/latest'
base_currency = 'USD'
target_currency = 'PLN'


api_key_crypto = 'b247350e-d4f6-4bb1-8860-c6d7365311af'
api_url_base_crypto = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

def get_info():
    response = requests.get(api_url_base + '?access_key=' + api_key)
    
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    return None


def get_rate():
    info = get_info()

    if info != None:
        rates = info['rates']
        pln = rates['PLN']
        usd = rates['USD']

    return (pln/usd)

def get_crypto_values(api_url, api_key_crypto):
    
    parameters = {
        'start':'1',
        'limit':'5000',
        'convert':'USD'
    }
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key_crypto,
    }
    
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(api_url, params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return e

def save_crypto_to_json(api_url, api_key_crypto):
    with open('crypto_data.json', 'w') as file:
        json.dump(get_crypto_values(api_url, api_key_crypto), file)
        file.close()


def get_crypto_price(crypto_name, api_url_base_crypto, api_key_crypto):

    save_crypto_to_json(api_url_base_crypto, api_key_crypto)

    with open('crypto_data.json', 'r') as file:
        data = json.load(file)
        i = 0

        while data['data'][i]['symbol'] != crypto_name:
            i+=1

        return data['data'][i]['quote']['USD']['price']




print(get_crypto_price("BTC", api_url_base_crypto, api_key_crypto))