#!/usr/bin/env python
import csv, time, datetime, os, requests, sys, json
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from lib import config

endpoint = config.binance().get('BASE_API')
header = config.binance().get('HEADER')

def depth(symbol):
    global endpoint
    endpoint += '/api/v1/depth'
    param={'symbol':symbol}
    response = requests.get(endpoint, params=str(param))
    return ( response.json() )

# recent trades
def trades(symbol):
    global endpoint
    endpoint += '/api/v1/trades'
    param={'symbol':symbol}
    response = requests.get(endpoint, params=str(param))
    return ( response.json() )

# recent trades
def old_trades(symbol):
    global endpoint
    endpoint += '/api/v1/historicalTrades'
    param={'symbol':symbol}
    response = requests.get(endpoint, params=str(param))
    return ( response.json() )

# aggregate trades
def agg_trades(symbol):
    global endpoint
    endpoint += '/api/v1/aggTrades'
    param={'symbol':symbol}
    response = requests.get(endpoint, params=str(param))
    return ( response.json() )


if __name__ == "__main__":
  print(trades('LTCBTC'))

  # print (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  # print (config.binance().get('SECRET'))
