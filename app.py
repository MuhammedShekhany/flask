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
            if name=="buy":
                usdt_account_info =  client.get_asset_balance(asset='USDT')
                print("Spot Account Information usdt:")
                print(usdt_account_info['free'])
                symbol = 'ADAUSDT'  # The trading pair
                quantity_usdt = int(float(usdt_account_info['free']))  # The amount you want to buy
                print('name::::::',name)

                if quantity_usdt != 0 :
                    order = client.order_market_buy(
                        symbol=symbol,
                        quoteOrderQty=quantity_usdt
                    )
                    print(order)
                elif quantity_usdt != 0 :
                    print("usdt === 0")
               
            elif name=="sell":
                    ADA_account_info =  client.get_asset_balance(asset='ADA')
                    print("Spot Account Information ADA:")
                    print(ADA_account_info['free'])
                    symbolADA = 'ADAUSDT'  # The trading pair
                    quantity_ADA = int(float(ADA_account_info['free']))
                    print("quantity ada=")
                    print(quantity_ADA)
                    #ticker = client.get_symbol_ticker(symbol=symbolADA)
                    #last_price = float(ticker['price'])
                    #print('lastprice:')
                    #print(last_price)
                    #stop_price =round(last_price -(0.001 * last_price),4)  # 0.5% below the last price
                    #print('stop_price:')
                    #print(stop_price)
                    #take_profit_price =round(last_price+(0.0025 * last_price),4)  # 0.5% above the last price
                    #print('take_profit_price:')
                    #print(take_profit_price)
                    #stop_limit_time_in_force = 'GTC'
                    if quantity_ADA != 0 :

                        order1 = client.order_market_sell(
                            symbol=symbolADA,
                            quoteOrderQty=quantity_ADA
                        )
                        print(order1)
                    elif quantity_ADA == 0 :
                        print("ada === 0")
                    
                
    
    except BinanceAPIException as e:
        print(f"Binance API exception occurred: {e}")
    except BinanceRequestException as e:
        print(f"Binance request exception occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return jsonify({'message':'done  POST request.'})


if __name__ == '__main__':
    app.run(debug=True)
