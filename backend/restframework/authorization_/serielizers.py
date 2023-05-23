from rest_framework import serializers
from .models import login_model

class login_model_serielizer(serializers.ModelSerializer):
    class Meta:
        model = login_model
        fields = "__all__"