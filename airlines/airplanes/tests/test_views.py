from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Airplane
from ..serializers import AirplaneSerializer
from .mock_data import data_1, data_1_dict, data_1_invalid, \
                        data_5, data_11

class AirplanesTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.existing_data = Airplane.objects.create(
            airplane_id=3,
            passenger=95,
            fuel_capacity=600.000,
            fuel_consumption=1.069,
            flight_endurance=561.272,
        )

    def setUp(self):
        self.client = APIClient()
        self.data_1 = data_1
        self.data_1_list = data_1_dict
        self.data_1_invalid = data_1_invalid
        self.data_5 = data_5
        self.data_11 = data_11

    def test_create_ONE(self):
        url = reverse('airplanes:airplanes-list')
        response = self.client.post(url, self.data_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 2)

    def test_create_ONE_failed(self):
        url = reverse('airplanes:airplanes-list')
        response = self.client.post(url, self.data_1_invalid, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Airplane.objects.count(), 1)

    def test_create_one_with_dict(self):
        url = reverse('airplanes:airplanes-list')
        response = self.client.post(url, self.data_1_list, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 2)

    def test_create_many(self):
        url = reverse('airplanes:airplanes-list')
        response = self.client.post(url, self.data_5, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), 6)

    def test_create_exceeds_limit(self):
        url = reverse('airplanes:airplanes-list')
        response = self.client.post(url, self.data_11, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_list(self):
        url = reverse('airplanes:airplanes-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = AirplaneSerializer(Airplane.objects.all(), many=True).data
        self.assertEqual(response.data, serializer_data)

    def test_patch_one_airplane_id(self):
        air_obj = Airplane.objects.last()
        new_data = {
            "airplane_id": 99
        }
        response = self.client.patch(
            reverse("airplanes:airplanes-detail",
                    kwargs={'pk': air_obj.uid}), data=new_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Airplane.objects.last().airplane_id, 99)

    def test_patch_one_passenger(self):
        air_obj = Airplane.objects.last()
        new_data = {
            "passenger": 100
        }
        response = self.client.patch(
            reverse("airplanes:airplanes-detail",
                    kwargs={'pk': air_obj.uid}), data=new_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Airplane.objects.last().passenger, 100)

    def test_get_one(self):
        airplane_obj = Airplane.objects.last()
        existing_uid = airplane_obj.uid
        response = self.client.get(
            reverse("airplanes:airplanes-detail", kwargs={'pk': existing_uid}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_one(self):
        """
        Hard Deletion
        """
        airplane_obj = Airplane.objects.last()
        response = self.client.delete(
            reverse("airplanes:airplanes-detail", kwargs={'pk': airplane_obj.uid}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Airplane.objects.last(), None)
