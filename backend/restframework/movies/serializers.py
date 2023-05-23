from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Movie, Note
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = [
        #     'description', 
        #     'rating',
        # ]

    
    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError('Rating has to be between 1-10')
        return value
    
    def validate(self, data):
        if data['us_gross'] > data['worldwide_gross']:
            raise serializers.ValidationError('worlwide_gross cannot be less than us_gross')
        return data
    
    # def is_rating(self)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        # token['password'] = user.password
        # token['email'] = user.email
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class NotesSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"