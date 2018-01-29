#!/usr/bin/env python
import csv, time, datetime, os, requests, sys, json, logging
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from lib import config
def general.generate_endpoint(url):
    return config.binance().get('BASE_API') + url

def get_api_key():
    return config.binance().get('KEY')

# # enable REQUESTS logging
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

def depth(symbol):
    endpoint = general.generate_endpoint('/api/v1/depth')
    query={"symbol":symbol}
    response = requests.get(endpoint, params=query)
    return ( response.json() )

# recent trades
def trades(symbol):
    endpoint = general.generate_endpoint('/api/v1/trades')
    query={'symbol':symbol}
    response = requests.get(endpoint, params=query)
    return ( response.json() )

# recent trades
def old_trades(symbol):
    endpoint = general.generate_endpoint('/api/v1/historicalTrades')
    query={'symbol':symbol}
    header={"X-MBX-APIKEY": general.get_api_key()}
    response = requests.get(endpoint, params=query, headers=header)
    return ( response.json() )

# aggregate trades
def agg_trades(symbol):
    endpoint = general.generate_endpoint('/api/v1/aggTrades')
    query={'symbol':symbol}
    response = requests.get(endpoint, params=query)
    return ( response.json() )

def candlestick(symbol, interval):
    endpoint = general.generate_endpoint('/api/v1/klines')
    query={'symbol':symbol, 'interval':interval }
    response = requests.get(endpoint, params=query)
    return ( response.json() )


def ticker(symbol=None):
    endpoint = general.generate_endpoint('/api/v1/ticker/24hr')
    if symbol is None: # will return all symbols on exchange
        response = requests.get(endpoint)
    else: # will return price data of only chosen symbol
        query={'symbol':symbol }
        response = requests.get(endpoint, params=query)
    return ( response.json() )

def ticker_price(symbol=None):
    endpoint = general.generate_endpoint('/api/v3/ticker/price')
    if symbol is None: # will return all symbols on exchange
        response = requests.get(endpoint)
    else: # will return price data of only chosen symbol
        query={'symbol':symbol }
        response = requests.get(endpoint, params=query)
    return ( response.json() )

def book_ticker(symbol=None):
    endpoint = general.generate_endpoint('/api/v3/ticker/bookTicker')
    if symbol is None: # will return all symbols on exchange
        response = requests.get(endpoint)
    else: # will return price data of only chosen symbol
        query={'symbol':symbol }
        response = requests.get(endpoint, params=query)
    return ( response.json() )


if __name__ == "__main__":
  print( old_trades('LTCBTC') )

  # print (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  # print (config.binance().get('SECRET'))
