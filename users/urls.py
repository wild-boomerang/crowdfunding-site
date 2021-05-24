from django.urls import path, include
from .views import dashboard

urlpatterns = [
    path('<str:username>/', dashboard, name='dashboard'),
]
