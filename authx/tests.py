from django.test import TestCase
from .models import CustomUser

from rest_framework.test import APITestCase
from rest_framework import status

BASE_URL = "http://127.0.0.1:8000/"
API_V1 = "rest-api/v1"

class ModelsTest(TestCase):
    def setUp(self) -> None:
        payloud = {
            "username": "adam3",
            "email": "adam3@wp.pl",
            "password": "password"
        }
        CustomUser.objects.create_user(**payloud)
    def test_amount_models(self):
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.filter(is_admin=True).count(), 0)

# class ModelTestRest(APITestCase):
#
#     def test_create_user(self):
#         data = {
#             "username": "adam3",
#             "email": "adam3@wp.pl",
#             "password": "password"
#         }
#         url = f"{BASE_URL}{API_V1}/authx/users/"
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
