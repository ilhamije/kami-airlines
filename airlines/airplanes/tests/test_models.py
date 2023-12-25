from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from airplanes.models import Airplane


class AirplaneTest(TestCase):
    def setUp(self):
        self.data = [{
            'airplane_id': 19,
            'passenger': 125,
            'fuel_capacity': 200.000,
            'fuel_consumption': 0.204,
            'flight_endurance': 980.392,
        }]

    def create_airplane(self, airplane_id: int,
                            passenger: int,
                            fuel_capacity: int,
                            fuel_consumption: int,
                            flight_endurance: int):

        return Airplane.objects.create(
            airplane_id=airplane_id,
            passenger=passenger,
            fuel_capacity=fuel_capacity,
            fuel_consumption=fuel_consumption,
            flight_endurance=flight_endurance,
        )

    def data_map(self, data):
        airplane_id = data.get('airplane_id')
        passenger = data.get('passenger')
        fuel_capacity = data.get('fuel_capacity')
        fuel_consumption = data.get('fuel_consumption')
        flight_endurance = data.get('flight_endurance')
        return airplane_id, passenger, fuel_capacity, fuel_consumption, flight_endurance

    def test_airplane_creation(self):
        data_map = self.data_map(self.data[0])
        created = self.create_airplane(*data_map)
        self.assertTrue(isinstance(created, Airplane))
        self.assertEqual(created.passenger, 125)

    def test_negative_passenger(self):
        selected_data = self.data[0]
        selected_data['passenger'] = -10  # Setting passenger to a negative value
        data_map = self.data_map(selected_data)

        # Attempting to create an airplane with invalid passenger value
        with self.assertRaises(IntegrityError):
            created = self.create_airplane(*data_map)
            created.full_clean()  # Triggering validation

