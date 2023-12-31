from typing import Dict
from django.core.serializers import json
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# from django.core.serializers.json import Serializer

from rest_framework import serializers

from .models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airplane
        fields = ['uid', 'airplane_id', 'passenger',
                  'fuel_capacity', 'fuel_consumption', 'flight_endurance']

    def create(self, validated_data):
        return Airplane.objects.create(**validated_data)

    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def to_representation(self, instance: Airplane) -> Dict:
        data = super().to_representation(instance)
        data['fuel_capacity'] = f'{instance.fuel_capacity} liters'
        data['fuel_consumption'] = f'{instance.fuel_consumption} liters per min'
        data['flight_endurance'] = f'{instance.flight_endurance} minutes'
        data['created_at'] = self.get_created_at(instance)
        return data
