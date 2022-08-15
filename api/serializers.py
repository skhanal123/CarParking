from rest_framework import serializers
from .models import parkingRate

#This serializer is for price api endpoint
class parkingRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = parkingRate
        fields = ['price' ]

#This serializer is for rate api endpoint
class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = parkingRate
        fields = ['id', 'days', 'start_time', 'end_time', 'tz', 'price' ]


      
