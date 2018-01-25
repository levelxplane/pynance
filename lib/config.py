#!/usr/bin/env python
import os

def binance():
    return {
        'KEY': os.getenv('BINANCE_API', 'lol'),
        'SECRET': os.getenv('BINANCE_SECRET', 'poop')
    }
