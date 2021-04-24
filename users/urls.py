from django.urls import path, include
from .views import dashboard, register, Home

urlpatterns = [
    # path('dashboard/', dashboard, name='dashboard'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('register/', register, name='register'),
    path('', Home.as_view(), name='home'),
]
