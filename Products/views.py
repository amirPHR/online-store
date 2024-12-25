# Package of rest_framework 
from rest_framework import viewsets , filters 
import django_filters 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter
from rest_framework.pagination import PageNumberPagination  
from rest_framework import permissions 
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
# About Product
from .serializers import ProductSerializer
from .models import Products

# Pagination Class
class DefaultPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'  
    max_page_size = 100
    
# Filters of Product class
class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name = 'name' , lookup_expr = 'icontains') 
    category = django_filters.CharFilter(field_name = 'category' , lookup_expr = 'icontains') 
    price = django_filters.CharFilter(field_name = 'price' , lookup_expr = 'icontains') 

# Product View
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter] 
    search_fields = ['name' , 'description' , 'category' , 'price'] 
    ordering_fields = ['name' , 'category' , 'price']
    ordering = ['name']
    permission_classes = [IsAuthenticated]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination

    # just admin can add,change product
    def get_permissions(self):
        if (self.action == 'create') or (self.action == 'put') or (self.action == 'patch'):  
            return [permissions.IsAdminUser()]
        return super().get_permissions()