from django.db import models

class Website(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        pass