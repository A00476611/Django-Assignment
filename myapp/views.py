from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import Response
from rest_framework.decorators import api_view
from .serializers import HotelSerializer
from rest_framework import generics, filters

from myapp.models import Hotel

def home(request):
    return HttpResponse("<h1>Hello World</h1>")

@api_view(['GET', 'POST'])
def getHotels(request):
    if request.method == 'GET':
        hotels = HotelSerializer(Hotel.objects.all(), many=True).data
        return Response({"hotels_list":hotels})
    if request.method == 'POST':
        serialized_request_data = HotelSerializer(data=request.data)
        if(serialized_request_data.is_valid()):
            serialized_request_data.save()
            return Response({"message":"Added Successfully"})
        else:
            return Response({"message":"Unsuccessful Addition"})
        
class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]