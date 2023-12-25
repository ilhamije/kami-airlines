from math import log
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Airplane
from .serializers import AirplaneSerializer

class AirplaneList(APIView):
    serializer_class = AirplaneSerializer

    def get(self, request, format=None):
        airplane_obj = Airplane.objects.all()
        serializer = self.serializer_class(airplane_obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        srlzr = self.serializer_class(data=data, many=True)
        srlzr.is_valid(raise_exception=True)

        if isinstance(data, dict):
            data = [data]

        check_length = self.check_data_length(data)
        if check_length:
            return check_length

        calculated_data = self.calculate(data)
        serializer = self.serializer_class(data=calculated_data, many=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def check_data_length(self, data):
        if len(data)>10:
            return Response({"message":"Max data is 10"}, status=status.HTTP_400_BAD_REQUEST)

    def calculate(self, data):
        print('incoming_data: ', data)
        new_data = []
        for i in data:
            airplane_id = int(i.get('id'))
            passenger = int(i.get('passenger'))
            fuel_capacity = int(airplane_id) * 200
            fuel_consumption = round(log(airplane_id) * 0.80, 3) # liter per minute
            fuel_consumption_psg = round(int(passenger) * 0.002, 3) # liter per minute
            total_fuel_consumption = fuel_consumption + fuel_consumption_psg # liter per minute
            # Flight Endurance (in minutes) = Fuel Capacity / Fuel Consumption Rate
            flight_endurance = round(fuel_capacity/total_fuel_consumption, 3)

            item = {}
            item['airplane_id'] = airplane_id
            item['passenger'] = passenger
            item['fuel_capacity'] = fuel_capacity
            item['fuel_consumption'] = total_fuel_consumption
            item['flight_endurance'] = flight_endurance

            new_data.append(item)
        return new_data