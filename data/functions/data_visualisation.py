from utils.config import EMA, SMA

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show_graph(df, max_rows=100, patterns=None):
    if max_rows > 100:
        print('You should display a maximum number of 150 candlestick to maintain a good readability in the graph')

    df = df.iloc[-max_rows:]
    df['datetime'] = pd.to_datetime(df['datetime'])

    fig = make_subplots(
        rows=2, 
        cols=1, 
        shared_xaxes=True, 
        vertical_spacing=0.1, 
        row_heights=[0.80, 0.2],
        subplot_titles=('Trading Graph', 'RSI')
    )
    
    fig.add_trace(go.Candlestick(
        x=df['datetime'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        name='Candlestick'
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=df['datetime'],
        y=df['average'],
        mode='lines',
        name='Average',
        line=dict(color='orange', width=2)
    ))

    for ema in EMA:
        fig.add_trace(go.Scatter(
            x=df['datetime'],
            y=df['ema' + str(ema['value'])],
            mode='lines',
            name='EMA' + str(ema['value']),
            line=dict(color=ema['color'], width=2)
        ))

    for sma in SMA:
        fig.add_trace(go.Scatter(
            x=df['datetime'],
            y=df['sma' + str(sma['value'])],
            mode='lines',
            name='SMA' + str(sma['value']),
            line=dict(color=sma['color'], width=2)
        ))

    fig.add_trace(go.Scatter(
        x=df['datetime'],
        y=df['rsi'],
        mode='lines',
        name='RSI',
        line=dict(color='purple', width=2)
    ), row=2, col=1)

    # Update layout
    fig.update_layout(
        title='Trading Graph with RSI',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False,
        yaxis2_title='RSI',
        yaxis2=dict(range=[0, 100])
    )

    fig.add_shape(
        type="line",
        x0=df['datetime'].iloc[0],
        x1=df['datetime'].iloc[-1],
        y0=70,
        y1=70,
        line=dict(color="grey", width=1, dash="dash"),
        row=2, col=1
    )

    fig.add_shape(
        type="line",
        x0=df['datetime'].iloc[0],
        x1=df['datetime'].iloc[-1],
        y0=30,
        y1=30,
        line=dict(color="grey", width=1, dash="dash"),
        row=2, col=1
    )

    if patterns:
        for fair_value_gap in patterns['Fair Value Gaps']:
            if fair_value_gap['Still Valid']:
                time_interval = (df['datetime'].iloc[1] - df['datetime'].iloc[0]).total_seconds()
                extension_seconds = 7 * time_interval # Extend the rectangle size to see it
                new_end_time = pd.to_datetime(fair_value_gap['End datetime']) + pd.to_timedelta(extension_seconds, unit='s')
                
                fig.add_shape(
                    type="rect",
                    x0=fair_value_gap['Begin datetime'],
                    y0=min(fair_value_gap['Begin price'], fair_value_gap['End price']),
                    x1=new_end_time,
                    y1=max(fair_value_gap['Begin price'], fair_value_gap['End price']),
                    line=dict(color="Blue", width=2),
                    fillcolor="rgba(0,0,255,0.2)"
                )

    fig.update_layout(
        title='Trading Graph',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False
    )

    fig.show()