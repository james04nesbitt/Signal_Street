import yfinance as yf


def get_data(ticker):
    data = yf.Ticker(ticker).info
    return data

