
import cbpro
import os
import pandas as pd
#import talib as ta
import time
import streamz
from streamz import Stream
from streamz.dataframe import DataFrame
import holoviews as hv
from holoviews import opts
from holoviews.streams import Buffer
from holoviews.plotting.links import RangeToolLink
from cb_websocket import coinbaseWebSocketClient as cws

class CryptoTradingBot:
    
    def __init__(self):
        self.client = cbpro.AuthenticatedClient(os.environ.get('COINBASE_SANDBOX_API_PUBLIC_KEY'), 
                                            os.environ.get('COINBASE_SANDBOX_API_SECRET_KEY'), 
                                            os.environ.get('COINBASE_SANDBOX_API_PASSPHRASE'), 
                                            api_url="https://api-public.sandbox.pro.coinbase.com")
        self.setupWebSockClient()


    def setupWebSockClient(self):
        self.ws_client = cws.coinbaseWebSocketClient()


    def run(self):
        self.ws_client.start()
    

    def trade(self, action, limitPrice, quantity):
        if action == 'buy':
            self.client.buy(price=limitPrice,
                            size=quantity,
                            order_type='limit',
                            product_id='BTC-USD',
                            overdraft_enabled=False)
        elif action == 'sell':
            self.client.sell(price=limitPrice,
                            size=quantity,
                            order_type='limit',
                            product_id='BTC-USD',
                            overdraft_enabled=False)

    def viewAccounts(self, accountCurrency):
        accounts = self.client.get_accounts()
        print(accounts)
        #account = list(filter(lambda x: x['currency'] == accountCurrency, accounts))[0]
        return accounts


    def viewOrder(self, order_id):
        pass


    def getCurrentPrice(self):
        tick = self.client.get_product_ticker(product_id='BTC-USD')
        return tick['bid']


if __name__ == "__main__":
    tradingSystem = CryptoTradingBot()
    tradingSystem.run()

    try: 
        while True:
            print("Message Count = ", "%i \n" % tradingSystem.ws_client.message_count)
            time.sleep(1)
    except KeyboardInterrupt:
        tradingSystem.ws_client.close()
