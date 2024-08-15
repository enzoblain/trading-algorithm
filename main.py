from data.data_manager import check_data
from data.data_fetcher import get_forex_candlestick_data

def main():
    check_data('1day')

if __name__ =="__main__":
    main()