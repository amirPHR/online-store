# Package imports
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import django_filters
# About Product class   
from .models import Products
from .serializers import ProductSerializer

# Pagination Class
class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Filters of Product class
class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category', lookup_expr='icontains')  
    price = django_filters.NumberFilter(field_name='price')  

    class Meta:
        model = Products
        fields = ['name', 'category', 'price']

# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.filter()  
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'description', 'category__name', 'price']
    ordering_fields = ['name', 'category__name', 'price']
    ordering = ['name']
    permission_classes = [IsAuthenticated]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination

    # Permissions: Only admins can create/update/delete products
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return super().get_permissions()