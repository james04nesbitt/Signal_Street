import vectorbt
import pandas as pd


data = bt.get('spy', start='2010-01-01')
sma = data.rolling(50).mean()
plot = bt.merge(data, sma).plot(figsize=(15, 5))
plot