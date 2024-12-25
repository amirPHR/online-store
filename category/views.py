# Package of rest_framework 
from rest_framework import viewsets 
from rest_framework.filters import SearchFilter , OrderingFilter 
import django_filters 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.pagination import PageNumberPagination 
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
# About Category 
from .models import Category 
from .serializers import CategorySerializer 

# Pagination Class
class DefaultPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'  
    max_page_size = 100  

# Filters 
class CategoryFilters(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name = 'name' , lookup_expr = 'icontains')
    description = django_filters.CharFilter(field_name = 'description' , lookup_expr = 'icontains')
    
# ViewSet 
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer     
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    search_fields = ['name' , 'description'] 
    ordering_fields = ['name' , 'description'] 
    ordering = ['name']  
    filterset_class = CategoryFilters 
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if (self.action == 'create') or (self.action == 'put') or (self.action == 'patch'):  
            return [permissions.IsAdminUser()]
        return super().get_permissions()