from django.db import models


class Order(models.Model):
    order_id = models.IntegerField()
    price_s = models.FloatField()
    price_rub = models.FloatField()
    delivery_date = models.DateTimeField()
