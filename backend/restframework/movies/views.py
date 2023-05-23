# django imports 
from django.http import JsonResponse
# DRF import
from rest_framework import permissions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# jwt
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# local imports 
from .serializers import MovieSerializer, NotesSerializer
from .models import Movie, Note

# Create your views here.
class class_api_movies(APIView):

    """
    DRF API authentication and authorization
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classe = [permissions.IsAuthenticated]
   

    def get(self, request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        authentication_classes = [authentication.TokenAuthentication]
        permission_classe = [permissions.IsAuthenticated]

        # data = {"first name": "Isaac", "last name": "Kyalo", "age": 22}
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET'])
def function_api_movies(request, *args, **kwargs):
    instance = Movie.objects.all()
    data = {}    
    # for index in range(len(instance)):
    #         print(f"{instance[index].title}\n{instance[index].description}\n{instance[index].rating}\n\n")
    try:
        if instance:
            data = MovieSerializer(instance, many=True).data
            return Response(data)
    except Exception as e:
        data.update({"Error": str(e)})
        return Response(data)


class api_authentication_tokens(APIView):
    def get(self,request):
        routes = [
            '/api/token',
            '/api/token/refresh'
        ]
        return Response(routes)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # add custom claims
        # token['name'] = user.name
        token['username'] = user.username

class PairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class Notesview(APIView):
    permission_classes = [permissions.IsAdminUser]
   
    def get(self, request):
        # instance = Note.objects.get(id=1)
        user = request.user
        # queryset = Note.objects.all()
        queryset = user.note_set.all()
        print(queryset)
        serializer = NotesSerializer(queryset, many=True)  
        return Response(serializer.data)

    def post(self, request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        # return Response({"Error": "data could not be saved"})

    