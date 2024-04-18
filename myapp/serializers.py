from rest_framework import serializers

from myapp.models import Hotel

class HotelSerializer(serializers.ModelSerializer) : 
    class Meta :
        model = Hotel
        fields = "__all__"
        #fields = ['id','name','price']