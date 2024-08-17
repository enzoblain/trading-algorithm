from analysis.candle import get_direction

def is_fair_value_gap(candles):
    if len(candles) != 3:
        return False

    if get_direction(candles[0]) != get_direction(candles[1]) and get_direction(candles[1]) != get_direction(candles[2]):
        return False

    return True