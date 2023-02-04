from django.test import TestCase, Client
from orders.models import Order
from django.urls import reverse


class OrderTest(TestCase):
    fixtures = ['orders.json', 'customers.json']

    def setUp(self):
        self.client = Client()
        self.test_data = {"customer": 1, "robot_serial": "A8-R5"}

    def test_order_create(self):
        response = self.client.post(reverse('create_order'), self.test_data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Order.objects.get(robot_serial=self.test_data['robot_serial']))
