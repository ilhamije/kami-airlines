from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Airplane
from ..serializers import AirplaneSerializer
from .mock_data import data_1, data_1_dict, data_5, data_11

class AirplanesTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.data_1 = data_1
        self.data_5 = data_5
        self.data_11 = data_11
        self.data_1_list = data_1_dict

    def test_create_ONE(self):
        url = reverse('airplanes:airplanes-list')
        response = self.client.post(url, self.data_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 1)

    def test_create_one_with_dict(self):
        url = reverse('airplanes:airplanes-list')
        response = self.client.post(url, self.data_1_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 1)

    def test_create_many(self):
        url = reverse('airplanes:airplanes-list')
        response = self.client.post(url, self.data_5, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 5)

    def test_create_exceeds_limit(self):
        url = reverse('airplanes:airplanes-list')
        response = self.client.post(url, self.data_11, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
