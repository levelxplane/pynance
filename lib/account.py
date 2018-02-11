#!/usr/bin/env python
import csv, time, datetime, os, requests, sys, json, logging, hmac
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from hashlib import sha256
from lib import config, general, query

# enable REQUESTS logging
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True


def info():
    endpoint=general.generate_endpoint('/api/v3/account')
    print (type(endpoint), endpoint)

    query_body = query.generate_param(True)
    # query_body = dict({'timestamp':'1517104969673','signature':'b98626ee18afd9112a649351ed6dbd94744fe48be82fc907a205d3f870262a1f'})
    header=dict({"X-MBX-APIKEY": general.get_api_key()})
    # print (type(query_body), type(header), query_body, header)
    response = requests.get(endpoint, headers=header, params=query_body)
    return ( response.json() )

def all_orders(symbol):
    endpoint=general.generate_endpoint('/api/v3/allOrders')
    print (type(endpoint), endpoint)

    # query_body = query.generate_param(True, symbol="XRPBTC")
    query_body = query.generate_param(True, **{"symbol":symbol})
    # query_body = dict({'timestamp':'1517104969673','signature':'b98626ee18afd9112a649351ed6dbd94744fe48be82fc907a205d3f870262a1f'})
    header=dict({"X-MBX-APIKEY": general.get_api_key()})
    # print (type(query_body), type(header), query_body, header)
    response = requests.get(endpoint, headers=header, params=query_body)
    return ( response.json() )


if __name__ == "__main__":
    # print(info())
    print(json.dumps(all_orders("XRPBTC"), indent=1))


  # print (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  # print (config.binance().get('SECRET'))
