# Package imports
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
import django_filters
# About Cart class
from .models import Cart
from .serializers import CartSerializer 

# Pagination Class
class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Cart Filter
class CartFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    product = django_filters.CharFilter(field_name='product__name', lookup_expr='icontains')
    quantity = django_filters.NumberFilter()

# CartViewSet
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CartFilter
    search_fields = ['user__username', 'product__name', 'quantity']
    ordering_fields = ['user__username', 'product__name', 'quantity']
    ordering = ['user']
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated]

    # Override the get_queryset method to only return the user's cart items
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)