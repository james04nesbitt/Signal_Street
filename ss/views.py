from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import TickerForm,StockForm
from .models import  Ticker
from .finance import get_tick
from .chart import get_chart, closing_price
from .finmodel import get_data
from .finnews import get_news

def index(request):
    context = {}
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            if ticker[0] !=  "{" or ticker[1] == '}':
                return HttpResponseRedirect("stock/"+ticker)
        else:
            form = TickerForm()
    context['sp500'] = get_chart("^GSPC","S&P500")
    context['dow'] = get_chart("^DJI", "Dow Jones Industrial Average")
    context['nas'] = get_chart("^IXIC","Nasdaq Composite")
    try:
        context['gainers'] = get_data("stock_market/gainers")[:10]
        context['losers'] = get_data("stock_market/losers")[:10]
        context['active'] = get_data("stock_market/actives")[:10]
    except:
        context['gainers'] = {}
        context['losers'] = {}
        context['active'] = {}

    context['news'] = get_news()[:15]
    for news in context['news']:
        news['headline'] = news['headline'].upper()
        if news['headline'][0] == ':':
            news['headline'] = news['headline'][2:]

    p = Ticker.objects.all()
    p = set([str(n) for n in p])
    portfolio = []
    for i in p:
        data = {}
        try:
            data['ticker'] = i.upper()
            stock = closing_price(i)
            price = round(stock[0]['Adj Close'][-1],2)
            data['price'] = "$"+ str(price)
            if data['price'][-2] == '.':
                data['price'] +='0'
            data['perchange'] = stock[3]+'%'
            data['amchanged'] = stock[2]
            data['pos'] = stock[2][0] == '+'


            portfolio.append(data)

        except:
            continue



    context['pf'] = portfolio

    return render(request, 'templates/index.html', context)


def ticker(request, tid):
    context = {}
    if tid[0] == "{":
        return render(request, 'ticker.html', context)
    if tid == 'index' or tid == 'markets':
        return HttpResponseRedirect('/')


    if request.method == 'POST':
        if 'add' in request.POST:
            T = Ticker()
            T.tick = tid
            T.save()
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
        else:
            form = TickerForm()
    context['form'] = TickerForm()
    data = get_tick(tid)
    context['ticker'] = tid.upper()
    context["name"] = data["longName"]
    context['price'] = data["currentPrice"]
    context["info"] = data["longBusinessSummary"]
    context['graph'] = get_chart(tid, context["name"])
    return render(request, 'ticker.html', context)

def markets(request):
    context = {}
    try:
        context['secperf'] = get_data('sector-performance')
    except:
        context['secperf'] = {}
    return  render(request, 'globe.html', context)




