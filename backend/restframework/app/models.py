from django.db import models

# Create your models here.
class api_model(models.Model):
    name_api = models.CharField(max_length=200, null=False, blank=False)
    type_api = models.CharField(max_length=200, default='GET')

    def __str__(self):
        return f'{self.name_api.capitalize()}'
    
    @property
    def _name_(self):
        return self.name_api

    @property
    def _type_(self):
        return self.type_api
    
