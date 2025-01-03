from rest_framework import serializers 
from .models import Address 

class AddressSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta: 
        model = Address 
        fields = ['id' , 'user' , 'country' , 'city' , 'address']