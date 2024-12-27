# Package imports
from rest_framework import viewsets , filters 
import django_filters 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.pagination import PageNumberPagination 
from rest_framework import permissions  
from rest_framework.permissions import IsAuthenticated
# About address class
from .models import Address 
from .serializers import AddressSerializer

# About pagination 
class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
# Address Filter 
class AddressFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains')
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')
    address = django_filters.CharFilter(field_name='address', lookup_expr='icontains')

    
# Address ViewSet 
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter] 
    search_fields = ['country' , 'city' , 'address']
    ordering_fields = ['country' , 'city' , 'address'] 
    ordering = ['country'] 
    pagination_class = DefaultPagination 
    permission_classes = [IsAuthenticated] 
    filterset_class = AddressFilter
    
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)   
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)