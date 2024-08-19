from utils.config import CONFIGURATION, TIMERANGES

from data.functions.data_manager import check_data
from data.functions.data_visualisation import show_graph
from analysis.analyze import analyze
from analysis.trend import get_trend_direction
import pandas as pd

def main():
    if CONFIGURATION['DATA_UPDATE']:
        for timerange in TIMERANGES:
            check_data(timerange)

    data = pd.read_csv('data/EUR-USD/5min.csv')
    data = data.iloc[-100:]

    patterns = analyze(data) 

    trends = get_trend_direction(data)

    show_graph(data, patterns=patterns, trends=trends)

if __name__ =="__main__":
    main()