#!/usr/bin/env python
import csv, time, datetime, os, requests, sys, json
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from lib import config

endpoint = config.binance().get('BASE_API')
header = config.binance().get('HEADER')

def ping():
    global endpoint
    endpoint += '/api/v1/ping'
    response = requests.get(endpoint)
    return ( response.json() )
    # print (header)

def servertime():
    global endpoint
    endpoint += '/api/v1/time'
    response = requests.get(endpoint)
    return ( int(response.json()['serverTime']) )

def info():
    global endpoint
    endpoint += '/api/v1/exchangeInfo'
    response = requests.get(endpoint)
    return ( response.json() )

if __name__ == "__main__":
  print()

  # print (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
  # print (config.binance().get('SECRET'))
