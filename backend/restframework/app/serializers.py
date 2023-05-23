from rest_framework import serializers
from .models import api_model

class apiModel_Serializer(serializers.ModelSerializer):
    # Name = serializers.SerializerMethodField(read_only=True)
    # Type = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = api_model
        fields = '__all__'
        # fields = [
        # "name_api",
        # "type_api",
        # ]

    # def get_Name(self, obj):
    #     return obj._name_

    # def get_Type(self, obj):
    #     return obj._type_
    