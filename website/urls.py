from django.urls import path
from django.urls.resolvers import URLPattern 

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.WebsiteListView.as_view(), name="home"),
    path('site/<int:pk>/', views.WebsiteDetailView.as_view(), name="detail"),
    path('site/<int:pk>/edit', views.WebsiteUpdateView.as_view(), name='edit')
]