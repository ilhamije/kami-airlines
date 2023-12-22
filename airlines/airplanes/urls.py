from django.urls import re_path
from .views import AirplaneList


app_name = "airplanes"

urlpatterns = [
    re_path('', AirplaneList.as_view(), name="airplanes-list"),
]
