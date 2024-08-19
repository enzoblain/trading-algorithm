from analysis.candle import get_average

def get_sma(candles):
    value = 0
    for candle in candles:
        value = value + get_average(candle)

    sma = value / len(candles)

    return round(sma, 5)

def get_ema(candles):
    smoothing_factor = 2/(len(candles))
    old_sma = get_sma(candles[:-1])
    ema = round((get_average(candles[-1]) - old_sma) * smoothing_factor + old_sma, 5)
    return ema

def get_ema(candles):
    initial_sma = get_sma(candles[:len(candles) - 1])
    smoothing_factor = 2 / (len(candles) + 1)
    current_price = get_average(candles[-1])
    ema = (current_price - initial_sma) * smoothing_factor + initial_sma
    
    return round(ema, 5)