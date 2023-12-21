from django.urls import re_path
from .views import AirplaneList


app_name = "airplane"

urlpatterns = [
    re_path('', AirplaneList.as_view(), name="airplane_list"),
]
