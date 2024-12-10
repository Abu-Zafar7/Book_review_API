from django.urls import path, include
from .views import RegisterView, BookViewSet, ReviewViewSet, BookRecommendationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Book Reviews API",
      default_version='v1',
      description="An API for managing books and reviews",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@bookreviews.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
 
    path('api/user/register/', RegisterView.as_view(), name='register'),
    path('api/user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path('api/', include(router.urls)),

    path('api/recommendations/', BookRecommendationView.as_view(), name='book-recommendations'),
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]