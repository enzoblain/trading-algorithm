from utils.config import CONFIGURATION, SYMBOL, COLUMNS, SMA
from calculs.candle import get_average
from calculs.sma import get_sma

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
        candles = data['values'][::-1]
        for index, candle in enumerate(candles):
            if 'average' not in COLUMNS:
                COLUMNS.append('average')
            candle['average'] = get_average(candle)
            for sma in SMA:
                if ('sma' + str(sma['value'])) not in COLUMNS:
                    COLUMNS.append('sma' + str(sma['value']))
                if index >= sma['value'] - 1:
                    candle['sma' + str(sma['value'])] = get_sma(candles[index - (sma['value'] - 1):index + 1])
                else: 
                    candle['sma' + str(sma['value'])] = ''

        df = pd.DataFrame(candles)

        df['datetime'] = pd.to_datetime(df['datetime'])
        df['datetime'] = df['datetime'].dt.tz_localize('Etc/GMT-10')
        df['datetime'] = df['datetime'].dt.tz_convert('Europe/Paris').dt.tz_localize(None)
        
        df.set_index('datetime', inplace=True)
        df = df[COLUMNS]
        return df
    else:
        print("Error:", data.get('message', 'Unknown error'))
        return None
