from rest_framework import serializers 
from .models import Products 

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Products 
        fields = ['id' , 'name' , 'description' , 'category' , 'price' , 'image' , 'created_at'] 
        
