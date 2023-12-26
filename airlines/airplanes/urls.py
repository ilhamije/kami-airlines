from django.urls import path
from .views import AirplaneList, AirplaneDetail


app_name = "airplanes"

urlpatterns = [
    path('', AirplaneList.as_view(), name="airplanes-list"),
    path('<str:pk>', AirplaneDetail.as_view(), name="airplanes-detail"),

]
