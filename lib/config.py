#!/usr/bin/env python
import os

def binance():
    return {
        'BASE_API': 'https://api.binance.com',
        'KEY': os.getenv('BINANCE_API', 'vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A'),
        'SECRET': os.getenv('BINANCE_SECRET', 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j')
    }
