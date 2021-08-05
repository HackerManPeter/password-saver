from django.urls import path
from django.urls.resolvers import URLPattern 

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.WebsiteListView.as_view(), name="home"),
]