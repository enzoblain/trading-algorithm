from utils.functions import get_from_env

API = {
    "KEY": get_from_env("TWELVE_DATA_API_KEY"),
    "URL": 'https://api.twelvedata.com/time_series'
}

SYMBOL = "EUR-USD"

TIMERANGES = [
    '1min',
    '5min',
    '15min',
    '30min',
    '1h',
    '4h',
    '1day',
    '1week'
]