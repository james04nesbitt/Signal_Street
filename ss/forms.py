from django import  forms
from .models import Ticker

class TickerForm(forms.Form):
    ticker = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'Ticker'}))

class StockForm(forms.ModelForm):
    class Meta:
        model = Ticker
        fields = ['tick']
