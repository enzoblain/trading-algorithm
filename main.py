from utils.config import TWELVE_DATA_API_KEY

import requests
import pandas as pd

API_KEY = TWELVE_DATA_API_KEY
BASE_URL = 'https://api.twelvedata.com/time_series'

def get_forex_candlestick_data(symbol, interval='5min'):
    params = {
        'symbol': symbol,
        'interval': interval,
        'apikey': API_KEY
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if 'values' in data:
        df = pd.DataFrame(data['values'])
        df['datetime'] = pd.to_datetime(df['datetime'])
        df.set_index('datetime', inplace=True)
        df = df[['open', 'high', 'low', 'close']]
        return df
    else:
        print("Error:", data.get('message', 'Unknown error'))
        return None

# Example usage
df = get_forex_candlestick_data('EUR/USD', '5min')
if df is not None:
    print(df.head())
else:
    print("Data retrieval failed.")
