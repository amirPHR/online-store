# Package imports 
from rest_framework import viewsets , filters 
import django_filters 
from django_filters.rest_framework import DjangoFilterBackend  
from rest_framework.filters import SearchFilter , OrderingFilter 
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# About comment
from .models import Comment 
from .serializers import CommentSerializer 

# Comment Pagination 
class CommentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    
# Comment Filter 
class CommentFilter(django_filters.FilterSet):
    user = django_filters.NumberFilter(field_name = 'user') 
    product = django_filters.NumberFilter(field_name = 'product')
    comment = django_filters.CharFilter(field_name = 'comment' , lookup_expr = 'icontains') 
    
# Comment ViewSet   
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    search_fields = ['user' , 'product' , 'comment']
    ordering_fields = ['user' , 'product' , 'comment'] 
    ordering = ['comment']
    pagination_class = CommentPagination 
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = CommentFilter