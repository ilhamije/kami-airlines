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
        fields = '__all__'

    def create(self, validated_data):
        return Airplane.objects.create(**validated_data)

    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def to_representation(self, instance: Airplane) -> Dict:
        data = super().to_representation(instance)
        data['created_at'] = self.get_created_at(instance)
        return data
