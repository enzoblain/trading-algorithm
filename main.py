from utils.config import CONFIGURATION, TIMERANGES

from data.data_manager import check_data
from data.data_visualisation import show_graph

import pandas as pd

def main():
    if CONFIGURATION['DATA_UPDATE']:
        for timerange in TIMERANGES:
            check_data(timerange)

    show_graph(pd.read_csv('data/EUR-USD/5min.csv'))

if __name__ =="__main__":
    main()