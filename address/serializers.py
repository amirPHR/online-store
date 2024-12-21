from rest_framework import serializers 
from .models import address 

class AddressSerializer(serializers.ModelSerializer):
    class Meta: 
        model = address 
        fields = ['user' , 'country' , 'city' , 'address']