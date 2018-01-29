#!/usr/bin/env python
import csv, time, datetime, os, requests, sys, json, logging, hmac
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from hashlib import sha256
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

# generate_param_body(True) generate signed signature key with only timestamp
# generate_param_body(True, foo1=bar1, foo2=bar2) signed with parameters
# generate_param_body(False, foo1=bar1, foo2=bar2) unsigned with parameters)
# generate_param_body(foo1=bar1, foo2=bar2) unsigned with parameters
# generate_param_body() unsigned no parameters
def generate_param(signature=False, **kwargs):
    x = dict(generate_param_body(dict(kwargs), signature))
    return x

def generate_param_body(param_dict, signature):
    timestamp=str(general.servertime())
    param_dict['timestamp']=timestamp
    if signature:
        param_dict['signature']=generate_signature(param_dict)
        print ('BODY TRUE: ', param_dict )
        return param_dict
    else:
        print ('BODY FALSE: ', param_dict )
        return param_dict

def generate_signature(query_dict):
    tmp_query_string=''
    for x in query_dict.keys():
        tmp_query_string+=x+'='+query_dict[x]+'&'
    tmp_query_string=tmp_query_string[:-1]
    return hmac.new(get_api_secret().encode('utf-8'), tmp_query_string.encode('utf-8'), sha256).hexdigest()

    # # hardcoded values from API example
    # print (tmp_query_string, get_api_secret())
    # tmp_query=b'symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559'
    # tmp_secret=b'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'
    # return hmac.new(tmp_secret, tmp_query, hashlib.sha256).hexdigest()

if __name__ == "__main__":
    print( generate_param(True) )

  # print (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  # print (config.binance().get('SECRET'))
