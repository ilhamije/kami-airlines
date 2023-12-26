from django.contrib import admin
from .models import Airplane


class AirplaneAdmin(admin.ModelAdmin):
    list_display = ['uid', 'airplane_id', 'passenger',
                    'fuel_capacity', 'fuel_consumption', 'flight_endurance', 'created_at']

admin.site.register(Airplane, AirplaneAdmin)
