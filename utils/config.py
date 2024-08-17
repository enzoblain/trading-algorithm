from utils.functions import get_from_env

CONFIGURATION = {
    "API" : {
        "KEY": get_from_env("TWELVE_DATA_API_KEY"),
        "URL": 'https://api.twelvedata.com/time_series'
    },
    "DATA_UPDATE": 'update' # False to do nothing, 'update' to add the 5000 last candles if they are not already in, 'edit' to make the calculs for all the values if it wasn't done (for example if we had a column but we want to keep the oldest values)
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

COLUMNS = ['open', 'high', 'low', 'close']
SMA = [
    {
        'value': 10,
        'color': 'rgb(255, 233, 0)'
    },
    {
        'value': 20,
        'color': 'rgb(172, 178, 0)'
    }, {
        'value': 50,
        'color': 'rgb(118, 122, 0)'
    }
]