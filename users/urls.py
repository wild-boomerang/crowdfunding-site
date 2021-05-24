from django.urls import path, include
from .views import dashboard, Home

urlpatterns = [
    path('<str:username>/', dashboard, name='dashboard'),
    path('', Home.as_view(), name='home'),
]
