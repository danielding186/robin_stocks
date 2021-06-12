import robin_stocks.robinhood as r
from functools import wraps

import os
USERNAME = os.getenv("RH_USERNAME")
PASSWORD = os.getenv("RH_PASSWORD")

def refresh_token(func):
    """A decorator for indicating which methods require the user to be logged
       in."""
    @wraps(func)
    def login_wrapper(*args, **kwargs):
        r.authentication.refresh_accessToken()
        return(func(*args, **kwargs))
    return(login_wrapper)

class robinStock():
    def __init__(self):
        r.login(USERNAME, PASSWORD)

    @refresh_token
    def getStockInfo(self, symbol):
        return r.get_stock_quote_by_symbol(symbol)

    @refresh_token
    def getStockByID(self, id):
        return r.get_stock_quote_by_id(id)

if __name__ == '__main__':
    rb_stock = robinStock()
    mp = {'APPL': '450dfc6d-5510-4d40-abfb-f633b7d9be3e'}
    print(rb_stock.getStockByID(mp['APPL']))
