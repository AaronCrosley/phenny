#!/usr/bin/env python3
"""
stock.py - Phenny ticker checker
author: Aaron Crosley <acrosley108@gmail.com>

"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode

def _request(symbol, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    req = Request(url)
    resp = urlopen(req)
    return str(resp.read().decode('utf-8').strip())


def get_price(symbol):
    return _request(symbol, 'l1')


def stock(phenny, input):
	stock = str(get_price(input))
	phenny.say(stock)


stock.commands = ['stock']
stock.example = '.stock AAPL'

if __name__ == '__main__':
    print(__doc__.strip())