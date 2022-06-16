from django.test import TestCase
from rest_framework.test import APIClient
from http import HTTPStatus
from utils.web import get_orders


class TestOrders(TestCase):
    def setUp(self) -> None:
        self.raw_orders = get_orders()
        self.count = len(self.raw_orders)

    def test_orders_list(self):
        client = APIClient()
        response = client.get("/api/v1/orders/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data), self.count)
