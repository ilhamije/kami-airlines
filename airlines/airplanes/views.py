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
        serializer = self.serializer_class(data=request.data, many=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
