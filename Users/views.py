import django_filters
from .serializers import UserCreate
from .models import CustomUser 
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated , DjangoModelPermissions  ,IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
   
class DefaultPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'  
    max_page_size = 100  

class FilterUser(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name = 'username', lookup_expr = 'icontains')
    email = django_filters.CharFilter(field_name = 'email', lookup_expr = 'icontains')
    first_name = django_filters.CharFilter(field_name = 'first_name', lookup_expr = 'icontains')
    last_name = django_filters.CharFilter(field_name = 'last_name', lookup_expr = 'icontains')
    phone_number = django_filters.CharFilter(field_name = 'phone_number', lookup_expr = 'icontains')
    national_code = django_filters.CharFilter(field_name = 'national_code', lookup_expr = 'icontains')


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreate    
    filter_backends = [DjangoFilterBackend , filters.OrderingFilter , SearchFilter]
    search_fields = ['username', 'email' , 'first_name' , 'lastname' , 'phone_number' , 'national_code']
    ordering_fields = ['id' , 'username', 'email' , 'first_name' , 'lastname' , 'phone_number' , 'national_code']
    ordering = ['id']
    pagination_class = DefaultPagination
    filterset_class = FilterUser
    
    def get_queryset(self):
            if self.request.user.is_authenticated:
                return CustomUser.objects.filter(id=self.request.user.id)
            return CustomUser.objects.none()  

  