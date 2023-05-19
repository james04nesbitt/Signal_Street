from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TickerForm
from .finance import get_data
from .chart import get_chart

context = {}
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

    data = get_data(tid)
    context['ticker'] = tid
    context["name"] = data["longName"]
    context['price'] = data["currentPrice"]
    context["info"] = data["longBusinessSummary"]
    context['graph'] = get_chart(tid)
    return render(request, 'ticker.html', context)


