from django.urls import path, include
from .views import campaign_list, campaign_detail, campaign_new

app_name = 'campaign'

urlpatterns = [
    path('', campaign_list, name='campaign_list'),
    path('new/', campaign_new, name='campaign_new'),
    path('<slug:category_slug>/', campaign_list, name='campaign_list_by_category'),
    path('<slug:author_slug>/<slug:name_slug>/', campaign_detail, name='campaign_detail'),
]
