def is_fair_value_gap(candles):
    if len(candles) != 3:
        return False
    
    if candles[0]['close'] > candles[2]['open']:
        direction = 'Bearish'
    elif candles[0]['close'] < candles[2]['open']:
        direction = 'Bullish'
    else:
        direction = None
    
    if direction == 'Bearish':
        supposed_begin = candles[0]['low']
        supposed_end = candles[2]['high']
        if supposed_begin < supposed_end:
            return None
    elif direction:
        supposed_begin = candles[0]['high']
        supposed_end = candles[2]['low']
        if supposed_begin > supposed_end:
            return None
    else:
        return None

    fair_value_gap = {
        'Begin datetime': candles[0]['datetime'],
        'Begin price': supposed_begin,
        'End price': supposed_end,
        'End datetime': candles[2]['datetime']
    }

    return fair_value_gap