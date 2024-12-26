# Packages imports 
from rest_framework import viewsets, filters 
import django_filters 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter 
from rest_framework.pagination import PageNumberPagination 
from rest_framework import permissions 
from rest_framework.permissions import IsAuthenticated , BasePermission
# About Payment class 
from .models import Payment 
from .serializers import PaymentSerializer 

# About Pagination
class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100 
    
# About Filters
class PaymentFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    order = django_filters.CharFilter(field_name='order__id', lookup_expr='icontains')
    price = django_filters.NumberFilter(field_name='price')
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
    
# About Permissions
class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff
    
# About Payment ViewSet
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['user', 'order', 'price', 'status']
    ordering_fields = ['user', 'order', 'price', 'status']
    ordering = ['user']
    pagination_class = DefaultPagination
    filterset_class = PaymentFilter 
    permission_classes = [IsAuthenticated , IsOwnerOrAdmin] 