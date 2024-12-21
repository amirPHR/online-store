from django.urls import path , include
from . import views 
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'Users' , UserViewSet)

urlpatterns = [
    path('' , include(router.urls)),    
]
