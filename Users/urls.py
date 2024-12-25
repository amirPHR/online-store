from django.urls import path, include

from rest_framework.routers import DefaultRouter #Router

from .views import UserViewSet # UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # token

from drf_yasg import openapi #swagger
from drf_yasg.views import get_schema_view # view of swagger
from rest_framework import permissions # permissions for swagger

from category.views import CategoryViewSet # CategoryViewSet
from Products.views import ProductViewSet # ProductViewSet
from Cart.views import CartViewSet # CartViewSet 

# Default Router
router = DefaultRouter()
router.register(r'Users', UserViewSet) # users
router.register(r'Category' , CategoryViewSet) # category 
router.register(r'Product' , ProductViewSet) # product
router.register(r'Cart' , CartViewSet) # cart

# swagger schema_view
schema_view = get_schema_view(
    openapi.Info(
        title="Users API",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="amirmohammadghlmpr@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[],
)

# urlpatterns
urlpatterns = [
    path('', include(router.urls)),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Give token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),  # Corrected Swagger path
]
