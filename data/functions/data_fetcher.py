from utils.config import CONFIGURATION, SYMBOL, COLUMNS, SMA
from calculs.general import general_calculs

import requests
import pandas as pd


def get_forex_candlestick_data(interval='5min', start_date=None, end_date=None, data_to_calcul=None):
    if not data_to_calcul:
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
            candles = data['values'][::-1]
        else:
            print("Error:", data.get('message', 'Unknown error'))
            return None
        
    else:
        candles = data_to_calcul
        
    candles = general_calculs(candles)

    df = pd.DataFrame(candles)

    df['datetime'] = pd.to_datetime(df['datetime'])
    
    if not data_to_calcul:
        df['datetime'] = df['datetime'].dt.tz_localize('Etc/GMT-10')
        df['datetime'] = df['datetime'].dt.tz_convert('Europe/Paris').dt.tz_localize(None)
        
    df.set_index('datetime', inplace=True)
    df = df[COLUMNS]
    return df