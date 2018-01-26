#!/usr/bin/env python
import csv, time, datetime, os, requests, sys, json, logging
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from lib import config, general

endpoint = config.binance().get('BASE_API')
api_key = config.binance().get('KEY')
secret = config.binance().get('SECRET')

# # enable REQUESTS logging
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

def info():
    global endpoint
    endpoint += '/api/v3/ticker/bookTicker'
    if symbol is None: # will return all symbols on exchange
        response = requests.get(endpoint)
    else: # will return price data of only chosen symbol
        query={'symbol':symbol }
        response = requests.get(endpoint, params=query)
    return ( response.json() )


if __name__ == "__main__":
  print( ticker() )

  # print (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  # print (config.binance().get('SECRET'))
