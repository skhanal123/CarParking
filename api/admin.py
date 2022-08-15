from django.contrib import admin
from .models import parkingRate

# Register your models here..
@admin.register(parkingRate)
class parkingRateAdmin(admin.ModelAdmin):
    list_display = ['id', 'days', 'start_time', 'end_time', 'tz', 'price' ]



