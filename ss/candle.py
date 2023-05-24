import base64
import urllib.parse

import pandas as pd
import plotly.graph_objs as go
import yfinance as yf
import io




def get_chart(ticker, time):
    choice = ticker.upper()
    data = yf.download(tickers=choice, period= '5d', interval = '15m', rounding = True)
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high = data['High'], low = data['Low'], close =
    data['Close'], name = 'market data'))
    fig.update_layout(title=choice + 'share price', yaxis_title = 'StockPrice(USD)')
    fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list([dict(count=15, label='15m', step ='minute', stepmode ='backward'),
    dict(count=45, label='45m', step ="minute", stepmode ="backward"),
    dict(count=1, label='1h', step ="hour", stepmode ="backward"),
    dict(count=6, label='6h', step ='hour', stepmode ="backward"),
    dict(step='all')])))
    fig.show()

    buf = io.BytesIO()


get_chart('aapl', 'aapl')