from analysis.candle import get_candle_direction, get_extreme
from utils.functions import transform_dataframe_to_dict

def get_trend_direction(candles):
    candles = transform_dataframe_to_dict(candles)
    trends = []
    current_trend = None

    for index in range(len(candles)):
        candle = candles[index]
        candle_direction = get_candle_direction(candle)

        if index == 0:
            current_trend = {
                'type': candle_direction,
                'high': get_extreme(candle, 'high'),
                'low': get_extreme(candle, 'low'),
                'intra': get_extreme(candle, 'low') if candle_direction == 'bullish' else get_extreme(candle, 'high'),
                'start': candle['datetime'],
                'end': None
            }
            continue

        if current_trend['type'] == 'bullish':
            keepgoing = 'high'
            rollback = 'low'
            sign = 1
        else:
            keepgoing = 'low'
            rollback = 'high'
            sign = -1

        if candle_direction == current_trend['type']:
            current_trend[keepgoing] = max(current_trend[keepgoing], get_extreme(candle, keepgoing))
        else:
            # Check for trend reversal based on the candle's close relative to the intra level
            if (sign * (float(candle['close']) - current_trend['intra'])) < 0:
                current_trend['end'] = candle['datetime']
                trends.append(current_trend)

                current_trend = {
                    'type': candle_direction,
                    'high': get_extreme(candle, 'high'),
                    'low': get_extreme(candle, 'low'),
                    'intra': get_extreme(candle, rollback),
                    'start': candle['datetime'],
                    'end': None
                }
            else:
                current_trend['intra'] = get_extreme(candle, rollback)

    if current_trend:
        current_trend['end'] = candles[-1]['datetime']
        trends.append(current_trend)
    return trends