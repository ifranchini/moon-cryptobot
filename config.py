# Binance integration
import os
import base64

API_KEY = base64.b64decode(os.environ['BNB_KEY']).decode('utf-8')
API_SECRET = base64.b64decode(os.environ['BNB_SECRET']).decode('utf-8')

