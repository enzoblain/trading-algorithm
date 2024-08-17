from utils.config import CONFIGURATION, SYMBOL
from calculs.candle import get_average

import requests
import pandas as pd


def get_forex_candlestick_data(interval='5min', start_date=None, end_date=None):
    params = {
        'symbol': SYMBOL.replace('-', '/'),
        'interval': interval,
        'apikey': CONFIGURATION['API']['KEY'],
        'start_date': start_date,
        'end_date': end_date
    }
    
    response = requests.get(CONFIGURATION['API']['URL'], params=params)
    data = response.json()
    
    if 'values' in data:
        for index, candle in enumerate(data['values']):
            candle['average'] = get_average(candle)

        df = pd.DataFrame(data['values'])

        df['datetime'] = pd.to_datetime(df['datetime'])
        df['datetime'] = df['datetime'].dt.tz_localize('Etc/GMT-10')
        df['datetime'] = df['datetime'].dt.tz_convert('Europe/Paris').dt.tz_localize(None)
        
        df.set_index('datetime', inplace=True)
        df = df[['open', 'high', 'low', 'close', 'average']]
        return df
    else:
        print("Error:", data.get('message', 'Unknown error'))
        return None
