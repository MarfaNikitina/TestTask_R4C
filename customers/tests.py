from django.test import TestCase, Client
from django.urls import reverse
from customers.models import Customer


class CustomerTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_data = {"email": "1234@mail.ru", "name": "Ann"}

    def test_customer_create(self):
        response = self.client.post(reverse('create_customer'), self.test_data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Customer.objects.get(email=self.test_data['email']))
