from utils.config import CONFIGURATION, TIMERANGES

from data.data_manager import check_data
from data.data_visualisation import show_graph
from analysis.analyze import analyze

import json

import pandas as pd

def main():
    if CONFIGURATION['DATA_UPDATE']:
        for timerange in TIMERANGES:
            check_data(timerange)

    df = pd.read_csv('data/EUR-USD/5min.csv')
    df = df.iloc[-100:].to_dict(orient='records')

    patterns = analyze(df) 
    # json_patterns = pretty_json = json.dumps(patterns, indent=4)
    # print(json_patterns)   

    show_graph(pd.read_csv('data/EUR-USD/5min.csv'), patterns=patterns)

if __name__ =="__main__":
    main()