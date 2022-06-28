from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

from .views import UserCreateListView

urlpatterns = [
    path('signup', view= UserCreateListView.as_view(), name='Create_and_view_users'),
    path('login', view= TokenObtainPairView.as_view(), name='Login_and_obtain_token'),
    path('token/verify', view=TokenVerifyView.as_view(), name='Verify_token'),
    path('token/refresh', view=TokenRefreshView.as_view(), name='Refresh_token')
]
