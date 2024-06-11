#api_key = 'HMO6jdvndrJW6ZPywUndhrimAzT8EnT0q8CGIoqt2PJNFxZiKaLKTdlNk9MLRhpi'
#api_secret = 'rpKjZPz4zbyheueA7ImeRgc2DbFkGhOf1DKaeQeoRsqHLpuybqPzOVj6ALdVb450'

from binance.client import Client
from binance.exceptions import BinanceAPIException
from binance.exceptions import BinanceRequestException
import time
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/', methods=['POST'])
def handle_post():
    print("hello1")
    data = request.get_json()
    print(data)
    name = data.get('name')
    print('name:', name)
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    else:
        
        # Replace with your Binance API key and secret
        api_key = 'HMO6jdvndrJW6ZPywUndhrimAzT8EnT0q8CGIoqt2PJNFxZiKaLKTdlNk9MLRhpi'
        api_secret = 'rpKjZPz4zbyheueA7ImeRgc2DbFkGhOf1DKaeQeoRsqHLpuybqPzOVj6ALdVb450'

        # Create a Binance client
        client = Client(api_key, api_secret)

        client.API_URL = 'https://api.binance.com/api'
        server_time = client.get_server_time()
        client.timestamp_offset = server_time['serverTime'] - int(time.time() * 1000)

        # Get spot account information
    try:
            
            usdt_account_info =  client.get_asset_balance(asset='USDT')
            print("Spot Account Information usdt:")
            print(usdt_account_info['free'])
            symbol = 'XAIUSDT'  # The trading pair
            quantity_usdt = int(float(usdt_account_info['free']))  # The amount you want to buy
            print('name::::::',name)

            if quantity_usdt != 0 :
                order = client.order_market_buy(
                    symbol=symbol,
                    quoteOrderQty=quantity_usdt
                )
                print(order)
                #################################################################################
                XAI_account_info =  client.get_asset_balance(asset='XAI')
                print("Spot Account Information xai:")
                print(XAI_account_info['free'])
                symbolXAI = 'XAIUSDT'  # The trading pair
                quantity_XAI = int(float(XAI_account_info['free']))
                ticker = client.get_symbol_ticker(symbol=symbolXAI)
                last_price = float(ticker['price'])
                print('lastprice:')
                print(last_price)
                stop_price =round(last_price -(0.0025 * last_price),4)  # 0.5% below the last price
                print('stop_price:')
                print(stop_price)
                take_profit_price =round(last_price+(0.0020 * last_price),4)  # 0.5% above the last price
                print('take_profit_price:')
                print(take_profit_price)
                stop_limit_time_in_force = 'GTC'

                order1 = client.create_oco_order(
                    symbol=symbolXAI,
                    side=Client.SIDE_SELL,
                    quantity=quantity_XAI,
                    price=take_profit_price,
                    stopPrice=stop_price,
                    stopLimitPrice=stop_price,
                    stopLimitTimeInForce=stop_limit_time_in_force
                )
                print(order1)
            elif quantity_usdt != 0 :
                print("usdt === 0")
    
    except BinanceAPIException as e:
        print(f"Binance API exception occurred: {e}")
    except BinanceRequestException as e:
        print(f"Binance request exception occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return jsonify({'message':'done  POST request.'})


if __name__ == '__main__':
    app.run(debug=True)
