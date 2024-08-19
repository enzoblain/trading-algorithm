def get_candle_direction(candle):
    if candle['open'] > candle['close']:
        return 'Bearish'
    elif candle['open'] < candle['close']:
        return 'Bullish'
    else:
        return None

def get_average(candle):
    max_high = get_extreme(candle, 'high')
    min_low = get_extreme(candle, 'low')

    average = round((max_high + min_low) / 2, 5)

    return average

def get_extreme(candle, params='high'):
    if candle['trend'] == 'Bullish':
        return candle[params]
    else:
        if params == 'high':
            return candle['low']
        else:
            return candle['high']