import yfinance as yf


def get_tick(ticker):
    data = yf.Ticker(ticker).info
    return data

