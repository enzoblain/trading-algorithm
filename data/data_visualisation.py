import pandas as pd
import plotly.graph_objects as go

def show_graph(df, max_rows=100, patterns=None):
    if max_rows > 100:
        print('You should display a maximum number of 150 candlestick to maintain a good readability in the graph')

    df = df.iloc[-max_rows:]
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    # Create candlestick chart
    fig = go.Figure(data=[go.Candlestick(
        x=df['datetime'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        name='Candlestick'
    )])

    # Add rectangles if provided
    if patterns:
        for fair_value_gap in patterns['Fair Value Gaps']:
            time_interval = (df['datetime'].iloc[1] - df['datetime'].iloc[0]).total_seconds()
            extension_seconds = 7 * time_interval # Extend the rectangle size
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