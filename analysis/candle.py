def get_direction(candle):
    if candle['open'] > candle['close']:
        return 'Bearish'
    elif candle['open'] < candle['close']:
        return 'Bullish'
    else:
        return None