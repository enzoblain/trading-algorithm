import pandas as pd
import mplfinance as mpf


def show_graph(df, max_rows=150):
    if max_rows > 150:
        print('You should display a maximum number of 150 candlestick to maintain a good readability in the graph')
    df = df.iloc[-max_rows:]

    df['datetime'] = pd.to_datetime(df['datetime'])

    df.set_index('datetime', inplace=True)

    mpf.plot(df, type='candle', style='charles', title='Trading Graph', ylabel='Price')
