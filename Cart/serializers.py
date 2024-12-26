from rest_framework import serializers 
from .models import Cart 

class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Cart 
        fields = ['id' , 'user' , 'product' , 'quantity' , 'total_price']
        
    def get_total_price(self, obj):    
        return obj.quantity * obj.product.price