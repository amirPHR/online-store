# Package of rest_framework 
from rest_framework import viewsets , filters 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
# About Cart
from .models import Cart 
from .serializers import CartSerializer

# Pagination Class
class DefaultPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'  
    max_page_size = 100  


# CartViewSet 
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter] 
    search_fields = ['user' , 'product' , 'quantity'] 
    ordering_fields = ['user' , 'product'] 
    ordering = ['user'] 
    pagination_class = DefaultPagination 
    permission_classes = [IsAuthenticated] 