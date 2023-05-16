from django.db import models

class StockTicker(models.Model):
    question_text = models.CharField(max_length=30)
