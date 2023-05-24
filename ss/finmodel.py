
from urllib.request import urlopen


import certifi
import json

def get_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url,cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)
def getVal(string):
    return f"https://financialmodelingprep.com/api/v3/{string}?apikey=018a72d2dfb5a6063259b0e8aa2caee4"

def biggest_gains():
    return get_data(getVal("stock_market/gainers"))

def biggest_loss():
    return get_data(getVal("stock_market/losers"))


print(biggest_gains()[0][''])