from django.urls import path, include

from rest_framework.routers import DefaultRouter #Router

# Token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

# Swagger
from drf_yasg import openapi #swagger
from drf_yasg.views import get_schema_view # view of swagger                                
from rest_framework import permissions # permissions for swagger

# ViewSets
from .views import UserViewSet # UserViewSet
from category.views import CategoryViewSet # CategoryViewSet
from Products.views import ProductViewSet # ProductViewSet
from Cart.views import CartViewSet # CartViewSet 
from address.views import AddressViewSet # AddressViewSet 
from comments.views import CommentViewSet # CommentViewSet
from Order.views import OrderViewSet # OrderViewSet 
from payment.views import PaymentViewSet # PaymentViewSet

# Default Router
router = DefaultRouter()
router.register(r'users', UserViewSet) # users
router.register(r'category' , CategoryViewSet) # category 
router.register(r'product' , ProductViewSet) # product
router.register(r'cart' , CartViewSet) # cart
router.register(r'address' , AddressViewSet) # address 
router.register(r'comment' , CommentViewSet) # comment   
router.register(r'order' , OrderViewSet) # order
router.register(r'payment' , PaymentViewSet) # payment 

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