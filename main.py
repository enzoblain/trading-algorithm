from utils.config import TIMERANGES

from data.data_manager import check_data

def main():
    for timerange in TIMERANGES:
        check_data(timerange)

if __name__ =="__main__":
    main()