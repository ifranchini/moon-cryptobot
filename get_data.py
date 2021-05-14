from binance.client import Client
from config import API_KEY, API_SECRET

client = Client(API_KEY, API_SECRET)

# prices = client.get_all_tickers()
# print(prices)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_30MINUTE)

print(candles)