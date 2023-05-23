from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import apiModel_Serializer
from .models import api_model


class class_api_call(APIView):
    """
    DRF View
    """
    def get(self, *args, **kwargs):
        instance = api_model.objects.all()
        serielizer = apiModel_Serializer(instance, many=True)
        return Response(serielizer.data)
    
    def post(self,request):
        serielizer = apiModel_Serializer(data=request.data)
        if serielizer.is_valid():
            serielizer.save()
            return Response(serielizer.data, status=201)
        return {"Error": "Invalid data"}
            