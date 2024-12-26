from rest_framework import serializers 
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Payment 
        fields = ['user' , 'order' , 'price' , 'status' , 'payment_date']