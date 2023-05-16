from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TickerForm
from .finance import get_data

def index(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
        else:
            form = TickerForm()
    form = TickerForm()
    return render(request, 'index.html', {'form': form})


def ticker(request, tid):
    context = {}
    data = get_data(tid)
    context['ticker'] = tid
    context["name"] = data["longName"]
    context['price'] = data["currentPrice"]
    context["info"] = data["longBusinessSummary"]
    return render(request, 'ticker.html', context)
