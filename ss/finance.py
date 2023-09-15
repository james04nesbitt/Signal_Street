import yfinance as yf


def get_tick(ticker):
    data = yf.Ticker(ticker).info
    return data
def getRSI(ticker):
    df = yf.download(ticker, period='1mo')
    period = 5
    delta = df['Close'].diff()
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)
    average_gain = gains.rolling(window=period).mean()
    average_loss = losses.rolling(window=period).mean()
    relative_strength = average_gain / average_loss

    relative_strength = average_gain / average_loss
    rsi = 100 - (100 / (1 + relative_strength))
    df['RSI'] = rsi
    df['RSI'].fillna(method='ffill', inplace=True)
