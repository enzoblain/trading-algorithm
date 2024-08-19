import pandas as pd

def is_still_valid(data, pattern):
    data['datetime'] = pd.to_datetime(data['datetime'])
    cutoff_datetime = pd.to_datetime(pattern['End datetime'])
    data = data[data['datetime'] > cutoff_datetime]

    max_high = data['high'].max()
    min_low = data['low'].min()

    pattern_low = min(pattern['Begin price'], pattern['End price'])
    pattern_high = max(pattern['Begin price'], pattern['End price'])

    return (pattern_low > max_high ) or (pattern_high < min_low)