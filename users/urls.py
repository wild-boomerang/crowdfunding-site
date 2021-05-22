from django.urls import path, include
from .views import dashboard, Home

urlpatterns = [
    path('accounts/dashboard/', dashboard, name='dashboard'),
    path('', Home.as_view(), name='home'),
]
