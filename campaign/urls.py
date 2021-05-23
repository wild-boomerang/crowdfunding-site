from django.urls import path, include
from .views import campaign_list, campaign_detail

app_name = 'campaign'

urlpatterns = [
    path('', campaign_list, name='campaign_list'),
    path('<slug:category_slug>', campaign_list, name='campaign_list_by_category'),
    path('<slug:campaign_slug>/', campaign_detail, name='campaign_detail'),
]
