from django.db import models


class Order(models.Model):
    order_id = models.CharField(max_length=10)
    price_s = models.DecimalField(max_digits=20, decimal_places=2)
    price_rub = models.DecimalField(max_digits=20, decimal_places=2)
    delivery_date = models.DateTimeField()
