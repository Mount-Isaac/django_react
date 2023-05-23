from django.db import models

# Create your models here.
class login_model(models.Model):
    email = models.CharField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return f'{self.username.capitalize()}'