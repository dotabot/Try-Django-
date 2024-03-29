from django.urls import path
from accounts.views import (
    login_view,
    logout_view,
    register_view
)
from .views import (
    article_search_view,
    article_create_view,
    article_detail_view
)
app_name='articles'

urlpatterns = [
    path('', article_search_view,name='search'),
    path('create/', article_create_view,name='create'),
    path('<slug:slug>/', article_detail_view,name='detail'),
   
]
