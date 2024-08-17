from utils.config import COLUMNS, SMA
from calculs.candle import get_average
from calculs.sma import get_sma

def general_calculs(candles):
    for index, candle in enumerate(candles):
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

    return candles