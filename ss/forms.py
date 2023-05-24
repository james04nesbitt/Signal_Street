from django import  forms

class TickerForm(forms.Form):
    ticker = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'Ticker'}))