from rest_framework.views import APIView
from rest_framework.response import Response
from .serielizers import login_model_serielizer
from .models import login_model

class login_class_APIView(APIView):
    def get(self, *args, **kwargs):
        instance = login_model.objects.all()
        serielizer = login_model_serielizer(instance, many=True)
        return Response(serielizer.data)
    
    
    def post(self, request):
        serielizer = login_model_serielizer(data=request.data)
        if serielizer.is_valid():
            serielizer.save()
            return Response(serielizer.data, status=201)
        return Response({"Error:", "Invaliddata"})
        