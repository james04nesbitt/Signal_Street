
from urllib.request import urlopen

import yfinance as yf
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

    url = getVal(url)
    response = urlopen(url,cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)
def getVal(string):
    return f"https://financialmodelingprep.com/api/v3/{string}?apikey=018a72d2dfb5a6063259b0e8aa2caee4"






