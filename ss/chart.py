import base64
import urllib.parse

import pandas as pd
import yfinance as yf
from datetime import date, timedelta
from matplotlib import pyplot as plt
import io




def closing_price(ticker):
    A = pd.DataFrame(yf.download(ticker, period="1y"))
    Asset = A[['Adj Close']]
    col = 'green'
    if(A['Open'][0] > A['Open'][-1]):
        col = 'red'
    return [Asset,col]
def get_chart(Ticker):
    Start = date.today() - timedelta(365)
    Start.strftime('%Y-%m-%d')

    End = date.today() + timedelta(2)
    End.strftime('%Y-%m-%d')
    data = closing_price(Ticker)
    plt.figure(facecolor="darkgray")
    ax = plt.axes()
    ax.set_facecolor('gray')


    plt.plot(data[0], color=data[1], linewidth=2)
    plt.title(Ticker, color = data[1], fontsize = 22)
    plt.ylabel('Price ($)')
    plt.xlabel('Date')
    fig = plt.gcf()



    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    uri = base64.b64encode(buf.read())
    uri = uri.decode('utf-8')
    buf.close()
    return uri
