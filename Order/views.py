# Package Imports
from rest_framework import viewsets , filters 
import django_filters
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.pagination import PageNumberPagination 
from rest_framework import permissions 
# About Order   
from .models import Order 
from .serializers import OrderSerializer 

# About Pagination
class OrderPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
# About permissions
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff

    
# About Filters 
class OrderFilter(django_filters.FilterSet):
    user = django_filters.NumberFilter(field_name='user')
    status = django_filters.NumberFilter(field_name='status', lookup_expr='exact')
    cart = django_filters.ChoiceFilter(field_name='cart')
    address = django_filters.CharFilter(field_name='address')
    
# About ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter] 
    search_fields = ['user' , 'status' , 'cart' , 'address'] 
    ordering_fields = ['user' , 'status' , 'cart' , 'address'] 
    ordering = ['user']
    pagination_class = OrderPagination 
    permission_classes = [IsOwnerOrAdmin]
    filterset_class = OrderFilter
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)