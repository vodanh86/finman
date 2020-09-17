# jwtauth/urls.py

from django.urls import path, include  # new
from .views import registration
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', registration, name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # new
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),      # new
]