from django.shortcuts import render
from django.views import generic

from .models import Website

class WebsiteListView(generic.ListView):
    model = Website
    template_name = 'website\index.html'
    context_object_name = 'website'