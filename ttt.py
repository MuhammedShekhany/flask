""" from binance.client import Client
from binance.exceptions import BinanceAPIException
from binance.exceptions import BinanceRequestException
import time
# Replace with your Binance API key and secret
api_key = 'HMO6jdvndrJW6ZPywUndhrimAzT8EnT0q8CGIoqt2PJNFxZiKaLKTdlNk9MLRhpi'
api_secret = 'rpKjZPz4zbyheueA7ImeRgc2DbFkGhOf1DKaeQeoRsqHLpuybqPzOVj6ALdVb450'

        # Create a Binance client
client = Client(api_key, api_secret)
client.tld='us'

client.API_URL = 'https://api.binance.com/api'
server_time = client.get_server_time()
client.timestamp_offset = server_time['serverTime'] - int(time.time() * 1000)            
usdt_account_info =  client.get_asset_balance(asset='USDT')
print("Spot Account Information usdt:")
print(usdt_account_info['free'])
 """
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
