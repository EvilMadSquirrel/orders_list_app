from datetime import datetime
from rest_framework import viewsets

from orders.models import Order
from orders.serializers import OrderSerializer
from utils.web import get_orders, get_dollar_price


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        raw_orders = get_orders()
        dollar_price = get_dollar_price()
        for order in raw_orders:
            order_id = order[1]
            price_s = float(order[2])
            delivery_date = datetime.strptime(order[3], '%d.%m.%Y')
            price_rub = price_s * dollar_price
            existing_order = Order.objects.filter(order_id=order_id).all().first()
            if existing_order:
                existing_order.price_rub = price_rub
                existing_order.save()
            else:
                Order.objects.create(order_id=order_id, price_s=price_s, price_rub=price_rub, delivery_date=delivery_date,)

        return self.queryset
