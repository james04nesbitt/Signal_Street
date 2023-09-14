import finnhub
apikey = "chse4t9r01qr5ochvj2gchse4t9r01qr5ochvj30"
def get_news():
    n = finnhub.Client(apikey)
    return n.general_news('general',min_id=0)