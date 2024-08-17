from calculs.candle import get_average

def get_sma(candles):
    value = 0
    for candle in candles:
        value = value + get_average(candle)

    sma = value / len(candles)

    return round(sma, 5)