from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from django import urls

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
    fields = ['website_name', 'website_url', 'username', 'password']
    
    def get_success_url(self):
        website_id = self.kwargs['pk']
        return reverse_lazy('website:detail', args=[str(website_id)])

class WebsiteDeleteView(generic.DeleteView):
    model=Website
    template_name = 'website\delete.html'
    success_url= urls.reverse_lazy('website:home')

class WebsiteCreateView(generic.CreateView):
    model=Website
    template_name = 'website\create.html'
    fields = ['user','website_name', 'website_url', 'username', 'password']
    success_url=urls.reverse_lazy('website:home')