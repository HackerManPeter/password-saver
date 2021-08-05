from django.db import models
from django.urls import reverse

class Website(models.Model):
    website_name = models.CharField(max_length=100)
    website_url = models.URLField(max_length=50)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.website_name
    
    def get_absolute_url(self):
        return reverse('website:detail', args=[str(self.pk)])