from analysis.pattern_recognition.Fair_Value_Gap import is_fair_value_gap

def analyze(candles):
    patterns = {}
    fair_value_gaps = []
    for index, candle in enumerate(candles):
        if index == 0 or index == 1:
            pass
        else: 
            fair_value_gap =  is_fair_value_gap([candles[index - 2], candles[index - 1], candle])
            if fair_value_gap:
                fair_value_gaps.append(fair_value_gap)
    if patterns != []:
        patterns["Fair Value Gaps"] = fair_value_gaps
    else:
        patterns["Fair Value Gaps"] = None
    return patterns