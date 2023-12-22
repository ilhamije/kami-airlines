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
        response = self.check_data_length(request.data)
        if response:
            return response

        calculated_data = self.calculate(request.data)
        serializer = self.serializer_class(data=calculated_data, many=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def check_data_length(self, data):
        print(type(len(data)), len(data))
        if len(data)>10:
            return Response({"message":"Max data is 10"}, status=status.HTTP_400_BAD_REQUEST)

    def calculate(self, data):
        new_data = []
        for i in data:
            airplane_id = int(i.get('id'))
            passenger = int(i.get('passenger'))
            fuel_capacity = int(airplane_id) * 200
            fuel_consumption = round(log(airplane_id) * 0.80, 3) # liter per minute
            fuel_consumption_psg = round(int(passenger) * 0.002, 3) # liter per minute
            total_fuel_consumption = fuel_consumption + fuel_consumption_psg

            print('airplane_id: ', airplane_id)
            print('passenger: ', passenger)
            print('fuel_capacity: ', fuel_capacity)
            print('fuel_consumption: ', fuel_consumption)
            print('fuel_consumption_psg: ', fuel_consumption_psg)
            print('total_fuel_consumption: ', total_fuel_consumption)

            item = {}
            item['id'] = airplane_id
            item['passenger'] = passenger
            item['fuel_capacity'] = fuel_capacity
            item['fuel_consumption'] = total_fuel_consumption

            new_data.append(item)
        return new_data