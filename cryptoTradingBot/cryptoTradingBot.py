import cbpro
import os

class CryptoTradingBot:
    
    def __init__(self, cb_pro_client):
        self.client = cb_pro_client

    
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
    auth_client = cbpro.AuthenticatedClient(os.environ.get('COINBASE_SANDBOX_API_PUBLIC_KEY'), 
                                            os.environ.get('COINBASE_SANDBOX_API_SECRET_KEY'), 
                                            os.environ.get('COINBASE_SANDBOX_API_PASSPHRASE'), 
                                            api_url="https://api-public.sandbox.pro.coinbase.com")

    tradingSystem = CryptoTradingBot(auth_client)
    print(tradingSystem.viewAccounts('BTC'))