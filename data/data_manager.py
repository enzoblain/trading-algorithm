from data.data_fetcher import get_forex_candlestick_data
from utils.config import SYMBOL

import os

import pandas as pd

from datetime import datetime, timedelta, date

def check_data(time_interval):
    if not os.path.exists(f'data/{SYMBOL}'):
        os.mkdir(f'data/{SYMBOL}')

    today = datetime.now()
    tomorrow = today + timedelta(1)
    tomorrow = tomorrow + timedelta(hours=8) # Adjust the time to the right Timezone (for this API : UTC + 10)

    csv_path = f'data/{SYMBOL}/{time_interval}.csv'

    if not os.path.exists(csv_path):
        with open(csv_path, "w") as file:
            file.write('datetime,open,high,low,close')
            
    df = get_forex_candlestick_data(interval=time_interval, end_date=datetime.strftime(tomorrow, '%Y-%m-%d')) .iloc[::-1]

    csv_file = pd.read_csv(csv_path)

    last_date = datetime.strptime('0001-01-01 00:00:00', "%Y-%m-%d %H:%M:%S")

    if not csv_file.empty:
        last_date = datetime.strptime('2024-08-15 21:10:00', "%Y-%m-%d %H:%M:%S")

    with open(csv_path, 'a') as file:
        for _, row in df.iterrows():
            date_time = pd.Timestamp(row.name)
            values = str(row['open']) + ',' + str(row['high']) + ',' + str(row['low'])+ ',' + str(row['close'])
            if date_time > last_date:
                file.write('\n' + str(pd.Timestamp(row.name)) + ',' + values)
    
    return True