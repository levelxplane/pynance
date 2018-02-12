#!/usr/bin/env python
import csv, time, datetime, os, requests, sys, json, logging
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from lib import config, general

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

def candlestick(symbol, interval, limit=1):
    endpoint = general.generate_endpoint('/api/v1/klines')
    query={'symbol':symbol, 'interval':interval, 'limit':limit}
    response = requests.get(endpoint, params=query)

    tmp_list=[]
    for x in response.json():
        tmp_list.append({"openTime":x[0],
            "open":x[1],
            "high":x[2],
            "low":x[3],
            "close":x[4],
            "volume":x[5],
            "close_time":x[6],
            "quote_asset_volume":x[7],
            "number_of_trades":x[8],
            "taker_buy_base_asset_volume":x[9],
            "taker_buy_quote_asset_volume":x[10],
            "ignore":x[11]
        })
    return tmp_list


    # return ( response.json() )
# [
#   [
#     1499040000000,      // "Open time":x[],
#     "0.01634790",       // "Open":x[],
#     "0.80000000",       // "High":x[],
#     "0.01575800",       // "Low":x[],
#     "0.01577100",       // "Close":x[],
#     "148976.11427815",  // "Volume":x[],
#     1499644799999,      // "Close time":x[],
#     "2434.19055334",    // "Quote asset volume":x[],
#     308,                // "Number of trades":x[],
#     "1756.87402397",    // "Taker buy base asset volume":x[],
#     "28.46694368",      // "Taker buy quote asset volume":x[],
#     "17928899.62484339" // "Ignore":x[],
#   ]
# ]

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
