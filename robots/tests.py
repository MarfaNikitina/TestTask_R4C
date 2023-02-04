from django.test import TestCase, Client
from django.urls import reverse

from robots.models import Robot


class RobotTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_data = {"model": "G7", "version": "A8"}

    def test_robot_create(self):
        response = self.client.post(reverse('create_robot'), self.test_data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Robot.objects.get(model=self.test_data['model']))
