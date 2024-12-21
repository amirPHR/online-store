from rest_framework import serializers 
from .models import Products , Comment

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Products 
        fields = ['name' , 'description' , 'category' , 'price' , 'image' , 'created_at'] 
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user' , 'product' , ' comment' , 'created_at']