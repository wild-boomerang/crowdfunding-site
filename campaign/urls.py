from django.urls import path, include
from .views import campaign_list, campaign_detail, campaign_new, campaign_edit, campaign_delete, comment_edit, \
                   comment_delete

app_name = 'campaign'

urlpatterns = [
    path('', campaign_list, name='campaign_list'),
    path('new/', campaign_new, name='campaign_new'),
    path('<slug:category_slug>/', campaign_list, name='campaign_list_by_category'),
    path('<slug:author_slug>/<slug:name_slug>/', campaign_detail, name='campaign_detail'),
    path('<slug:author_slug>/<slug:name_slug>/edit/', campaign_edit, name='campaign_edit'),
    path('<slug:author_slug>/<slug:name_slug>/delete/', campaign_delete, name='campaign_delete'),
    path('<slug:author_slug>/<slug:name_slug>/comments/<int:comment_pk>/edit/', comment_edit, name='comment_edit'),
    path('<slug:author_slug>/<slug:name_slug>/comments/<int:comment_pk>/delete/', comment_delete, name='comment_delete'),
]
