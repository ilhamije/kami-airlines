from math import log
from abc import ABC
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Airplane
from .serializers import AirplaneSerializer


class CommonProcess(ABC):

    def check_data_length(self, data):
        if len(data)>10:
            return Response({"message":"Max data is 10"}, status=status.HTTP_400_BAD_REQUEST)

    def calculate(self, data):
        if isinstance(data, dict):
            data = [data]

        check_length = self.check_data_length(data)
        if check_length:
            return check_length


        new_data = []
        for i in data:
            airplane_id = int(i.get('airplane_id'))
            passenger = int(i.get('passenger'))
            fuel_capacity = int(airplane_id) * 200
            fuel_consumption = round(log(airplane_id) * 0.80, 3) # liter per minute
            fuel_consumption_psg = round(int(passenger) * 0.002, 3) # liter per minute
            consumption = fuel_consumption + fuel_consumption_psg  # liter per minute
            total_fuel_consumption = round(consumption, 3)
            flight_endurance = round(fuel_capacity/total_fuel_consumption, 3)

            item = {}
            item['airplane_id'] = airplane_id
            item['passenger'] = passenger
            item['fuel_capacity'] = fuel_capacity
            item['fuel_consumption'] = total_fuel_consumption
            item['flight_endurance'] = flight_endurance

            new_data.append(item)
        return new_data

    def validate_payload(self, data):
        if isinstance(data, dict):
            data = [data]
        srlzr = AirplaneSerializer(data=data, many=True)
        srlzr.is_valid(raise_exception=True)


class AirplaneList(APIView, CommonProcess):
    """
    Get All and Create One
    """
    serializer_class = AirplaneSerializer

    def get(self, request, format=None):
        airplane_obj = Airplane.objects.all()
        serializer = self.serializer_class(airplane_obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        self.validate_payload(data)

        calculated_data = self.calculate(data)
        serializer = self.serializer_class(data=calculated_data, many=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AirplaneDetail(APIView, CommonProcess):
    """
    Retrieve, Update or Delete
    """
    serializer_class = AirplaneSerializer

    def get(self, request, pk, format=None):
        print(request.data)
        airplane_obj = get_object_or_404(Airplane, pk=pk)
        serializer = self.serializer_class(airplane_obj)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        data = request.data

        airplane_obj = get_object_or_404(Airplane, pk=pk)
        existing_airplane_id = airplane_obj.airplane_id
        existing_passenger = airplane_obj.passenger
        if 'airplane_id' not in data:
            data['airplane_id'] = existing_airplane_id
        if 'passenger' not in data:
            data['passenger'] = existing_passenger

        self.validate_payload(data)
        calculated_data = self.calculate(data)
        serializer = self.serializer_class(airplane_obj, data=calculated_data[0], partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        airplane_obj = get_object_or_404(Airplane, pk=pk)
        airplane_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
