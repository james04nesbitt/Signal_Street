from django.urls import path

from . import views

urlpatterns = [
    path('stock/<str:tid>', views.ticker, name='ticker'),
    path("", views.index, name="index"),
    path('markets', views.markets, name = 'markets'),


]