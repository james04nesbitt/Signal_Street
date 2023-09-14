import base64
import urllib.parse

import pandas as pd
import yfinance as yf
from datetime import date, timedelta
from matplotlib import pyplot as plt
import io




def closing_price(ticker):
    A = pd.DataFrame(yf.download(ticker, period="1d", interval='1m'))

    Asset = A[['Adj Close']]

    col = 'green'
    open = A['Open'][0]
    if(open > A['Open'][-1]):
        col = 'red'
    amChanged = round(A['Adj Close'][-1] - open,2)
    perChanged = round(100 *(amChanged / open), 2)
    if amChanged >= 0:
        amChanged = '+' + str(amChanged)
        perChanged = '+' + str(perChanged)
    else:
        amChanged = str(amChanged)
        perChanged = str(perChanged)

    return [Asset,col,amChanged, perChanged]


def get_chart(Ticker, name, ):
    Start = date.today() - timedelta(365)
    Start.strftime('%Y-%m-%d')


    End = date.today() + timedelta(2)
    End.strftime('%Y-%m-%d')
    data = closing_price(Ticker)
    plt.figure(facecolor="#1f242d")
    ax = plt.axes()
    ax.set_facecolor('#1f242d')


    plt.plot(data[0], color=data[1], linewidth=2)
    plt.title(name +'\n'+ str(data[2]) + '(' + str(data[3]) + '%)', color = "#088F8F", fontsize = 19)
    plt.ylabel('Price ($)')
    plt.xlabel('Date')
    plt.axis('off')
    fig = plt.gcf()



    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    uri = base64.b64encode(buf.read())
    uri = uri.decode('utf-8')
    buf.close()
    return uri