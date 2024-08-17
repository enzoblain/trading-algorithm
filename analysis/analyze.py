from analysis.pattern_recognition.Fair_Value_Gap import is_fair_value_gap
from calculs.candle import get_average
from utils.functions import transform_dataframe_to_dict

def analyze(candles):
    candles_dict = transform_dataframe_to_dict(candles)

    patterns = {}
    fair_value_gaps = []
    for index, candle in enumerate(candles_dict):
        if index == 0 or index == 1:
            pass
        fair_value_gap =  is_fair_value_gap(candles, [candles_dict[index - 2], candles_dict[index - 1], candle])
        if fair_value_gap:
            fair_value_gaps.append(fair_value_gap)

    if patterns != []:
        patterns["Fair Value Gaps"] = fair_value_gaps
    else:
        patterns["Fair Value Gaps"] = None
    return patterns