from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    release_date = models.DateField()
    rating = models.PositiveSmallIntegerField()

    us_gross = models.IntegerField(default=0)
    worldwide_gross = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title.capitalize()}'


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    notes_body = models.TextField(null=True)

    def __str__(self):
        # return f'{self.notes_body}'
        return f'{" ".join(self.notes_body.capitalize().split(" ")[:3])}'

