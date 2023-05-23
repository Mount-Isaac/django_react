from django.test import TestCase
from rest_framework import serializers
from .models import Movie
# Create your tests here.

class MovieSerializer(serializers.ModelSerializer):
    model = Movie
    fields = '__all__'
