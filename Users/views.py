# Package imports
from rest_framework import viewsets
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser , AllowAny
# About User class
from .serializers import UserCreate
from .models import CustomUser 
   
# Pagination Class
class DefaultPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'  
    max_page_size = 100  

# Filters
class FilterUser(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
    first_name = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    phone_number = django_filters.CharFilter(field_name='phone_number', lookup_expr='icontains')
    national_code = django_filters.CharFilter(field_name='national_code', lookup_expr='icontains')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'national_code']

# ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreate    
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'national_code']
    ordering_fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'national_code']
    ordering = ['id']
    pagination_class = DefaultPagination
    filterset_class = FilterUser

    # Override get_queryset to filter based on user permissions
    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff:  
                return CustomUser.objects.all()
            return CustomUser.objects.filter(id=self.request.user.id)  
        return CustomUser.objects.none()

    # Override get_permissions to handle permissions based on action
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            if self.request.user.is_authenticated:
                if self.action == 'create':
                    return [IsAdminUser()]  
                if self.action in ['update', 'partial_update'] and self.kwargs.get('pk') != str(self.request.user.id):
                    return [IsAdminUser()]  
                return [IsAuthenticated()]  
            else:
                return [AllowAny()]  

        return super().get_permissions()