from django.contrib import admin
from django.urls import path
from freepapp import views
from freepapp.views import authenticate_user, get_user, logout_user
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenObtainPairView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('auth/authenticate_user/', authenticate_user, name='authenticate_user'),
    path('auth/get_user/', get_user, name='get_user'),
    path('auth/logout/', logout_user, name='logout_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]