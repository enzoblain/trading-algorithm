def get_average(candle):
    max_high = max(float(candle['open']), float(candle['high']), float(candle['low']), float(candle['close']))
    min_low = min(float(candle['open']), float(candle['high']), float(candle['low']), float(candle['close']))

    average = round((max_high + min_low) / 2, 5)

    return average