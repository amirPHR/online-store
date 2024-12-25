from rest_framework import serializers
from .models import CustomUser 
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
        
class CurrentUser(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id' , 'username', 'email' , 'password' , 'first_name' , 'last_name']
        ref_name = 'CurrentUser'    
        
class UserCreate(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id' , 'username' , 'email' , 'password' , 'first_name' , 'last_name' , 'phone_number' , 'national_code', 'job']