from data.functions.data_fetcher import get_forex_candlestick_data, update_forex_candlestick_data
from utils.config import SYMBOL, COLUMNS, CONFIGURATION
from utils.functions import transform_dataframe_to_dict

import os

import pandas as pd

from datetime import datetime, timedelta

def check_data(time_interval):
    if not os.path.exists(f'data/{SYMBOL}'):
        if CONFIGURATION['DATA_UPDATE'] == 'update':
            os.mkdir(f'data/{SYMBOL}')
        else:
            return

    today = datetime.now()
    tomorrow = today + timedelta(1)
    tomorrow = tomorrow + timedelta(hours=8) # Adjust the time to the right Timezone (for this API : UTC + 10)

    csv_path = f'data/{SYMBOL}/{time_interval}.csv'

    if CONFIGURATION['DATA_UPDATE'] == 'update':
        df = get_forex_candlestick_data(interval=time_interval, end_date=datetime.strftime(tomorrow, '%Y-%m-%d'))
    else:
        if not os.path.exists(csv_path):
            return 
        csv_dict = transform_dataframe_to_dict(pd.read_csv(csv_path))
        df = update_forex_candlestick_data(csv_dict)

    if not os.path.exists(csv_path) or pd.read_csv(csv_path).empty or CONFIGURATION['DATA_UPDATE'] == 'edit':
        with open(csv_path, "w") as file:
            file.write('datetime,' + ','.join(COLUMNS))

    csv_file = pd.read_csv(csv_path)
    csv_file.set_index('datetime', inplace=True)

    last_date = datetime.strptime('0001-01-01 00:00:00', "%Y-%m-%d %H:%M:%S")

    if not csv_file.empty:
        last_date = datetime.strptime(csv_file.iloc[-1].name, "%Y-%m-%d %H:%M:%S")

    with open(csv_path, 'a') as file:
        for _, row in df.iterrows():
            date_time = pd.Timestamp(row.name)
            values = ','.join([str(row[column]) for column in COLUMNS])
            if date_time > last_date or CONFIGURATION['DATA_UPDATE'] == 'edit':
                file.write('\n' + str(pd.Timestamp(row.name)) + ',' + values)
    
    return True