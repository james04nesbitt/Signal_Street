from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TickerForm
from .finance import get_data
from .chart import get_chart
from .finmodel import biggest_gains,biggest_loss

def index(request):
    context = {}
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
        else:
            form = TickerForm()
    context['form'] = TickerForm()
    context['sp500'] = get_chart("^GSPC","S&P500")
    context['dow'] = get_chart("^DJI", "Dow Jones Industrial Average")
    context['nas'] = get_chart("^IXIC","Nasdaq Composite")
    context['gainers'] = biggest_gains()
    context['losers'] = biggest_loss()
    return render(request, 'index.html', context)


def ticker(request, tid):
    context = {}
    data = get_data(tid)
    context['ticker'] = tid
    context["name"] = data["longName"]
    context['price'] = data["currentPrice"]
    context["info"] = data["longBusinessSummary"]
    context['graph'] = get_chart(tid, context["name"])
    return render(request, 'ticker.html', context)


