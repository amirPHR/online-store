from rest_framework import serializers 
from .models import Order 

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta: 
        model = Order 
        fields = ['id' , 'user' , 'status' , 'cart' , 'address']