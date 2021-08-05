from django.shortcuts import render
from django.views import generic

from .models import Website

class WebsiteListView(generic.ListView):
    model = Website
    template_name = 'website\index.html'
    context_object_name = 'website'

class WebsiteDetailView(generic.DetailView):
    model = Website
    template_name = 'website\detail.html'

class WebsiteUpdateView(generic.UpdateView):
    model = Website
    template_name = "website\edit.html"
    fields = {'website_name', 'website_url', 'username', 'password'}
