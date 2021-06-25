import cbpro
import time

class coinbaseWebSocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ["BTC-USD", "ETH-USD"]
        self.channels = ["ticker"]
        self.message_count = 0
    
    
    def on_message(self, msg):
        self.message_count += 1
        print(msg)
        if 'price' in msg and 'type' in msg:
            print ("Message type:", msg["type"],
                   "\t@ {:.3f}".format(float(msg["price"])))
    
    
    def on_close(self):
        print("-- Goodbye! --")
