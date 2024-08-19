from utils.config import COLUMNS, EMA, SMA
from analysis.candle import get_average, get_candle_direction
from calculs.moving_averages import get_ema, get_sma

def general_calculs(candles):
    for index, candle in enumerate(candles):
        if 'trend' not in COLUMNS:
            COLUMNS.append('trend')
        candle['trend'] = get_candle_direction(candle)
        if 'average' not in COLUMNS:
            COLUMNS.append('average')
        candle['average'] = get_average(candle)
        for sma in SMA:
            if ('sma' + str(sma['value'])) not in COLUMNS:
                COLUMNS.append('sma' + str(sma['value']))
            if index >= sma['value'] - 1:
                candle['sma' + str(sma['value'])] = get_sma(candles[index - (sma['value'] - 1):index + 1])
            else: 
                candle['sma' + str(sma['value'])] = ''
        
        for ema in EMA:
            if ('ema' + str(ema['value'])) not in COLUMNS:
                COLUMNS.append('ema' + str(ema['value']))
            if index >= ema['value'] - 1:
                candle['ema' + str(ema['value'])] = get_ema(candles[index - (ema['value'] - 1):index + 1])
            else: 
                candle['ema' + str(ema['value'])] = ''

    return candles