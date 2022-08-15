from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import parkingRateSerializer, RateSerializer
from rest_framework.generics import ListAPIView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .models import parkingRate
import json
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework.response import Response
from .timezoneweekday import findweekday, findtimezone


# This view class is used to retrieve the parking rates available in the system through the specified endpoint
# Only HTTP GET and PUT method are enabled so that user can only view and update the data as only 
class parkingRateViewset(viewsets.ModelViewSet):
    queryset = parkingRate.objects.all()
    serializer_class = RateSerializer
    http_method_names = ['get', 'put']


# This view function is used to retrieve the price of the parking as per the query parameters set by users through API end point
# Only GET method is enabled in the view function as there is no requirement of other HTTP methods for users at this API end poind
@api_view(['GET'])
def priceapi(request):
    start_time = request.query_params.get('start')
    end_time = request.query_params.get('end')
    b = datetime.fromisoformat(start_time)
    c = datetime.fromisoformat(end_time)
    tz_offset = start_time[-6:]
    isoday = str(b.weekday())
    weekday = findweekday(isoday)
    tz_name = findtimezone(tz_offset)
    stime = (b.hour)*100+(b.minute)
    etime = (c.hour)*100+(c.minute)
    if (c-b)>timedelta(days = 1):
        return Response({"Parking: Unavailable"})
    else:
        queryset = parkingRate.objects.filter(days__contains=weekday,tz__contains = tz_name, start_time__lte=stime, end_time__gte=etime).values('price')
        if queryset.exists():
            serializer = parkingRateSerializer(queryset, many = True)
            return Response(serializer.data)
        else:
            return Response({"Parking: Unavailable"})


# This view function is used for automatic upload of the parking rate jsonfile at the start of the application
# This function will remove the existing data and upload new data in the database as per the json file
# The parking rate json file to be kept inside static folder with the name "rates.json"
def JsonData(request):
    filepath = settings.STATIC_DIR + '/rates.json'
    with open(filepath, 'r') as f:
        my_json_obj = json.load(f)
    parkingRate.objects.all().delete()
    for i in my_json_obj:
        for k in my_json_obj[i]:
            objs = [
                parkingRate(
                days = k['days'],
                start_time = k['start_time'],
                end_time = k['end_time'],
                tz = k['tz'],
                price =  k['price']
                )
            ]
            parkingRate.objects.bulk_create(objs)
    return HttpResponse ("Data Upload Successfully")

