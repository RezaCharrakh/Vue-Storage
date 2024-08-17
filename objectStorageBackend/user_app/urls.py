from django.urls import path
from .views import create_user, verify_email, login_view

urlpatterns = [
    path('api/create_account', create_user, name='create_user'),
    path('verify-email/<str:verification_token>/', verify_email, name='verify-email'),
    path('login', login_view, name='login-view'),
]