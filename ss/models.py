from django.db import models

class StockTicker(models.Model):
    question_text = models.CharField(max_length=30)
class Portfolio(models.Model):
    name = models.CharField(max_length=30)
class Ticker(models.Model):
    tick = models.CharField(max_length=50)
    def __str__(self):
        return self.tick

