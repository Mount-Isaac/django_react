from django.urls import path
from .views import (
    class_api_movies, 
    function_api_movies,
    api_authentication_tokens,
    Notesview
    )
from .serializers import CustomTokenObtainPairView
from rest_framework_simplejwt.views import  TokenRefreshView

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Movie API')

urlpatterns = [
    path('movies/class/', class_api_movies.as_view(), name="class-based"),
    path('movies/func/', function_api_movies, name="func-based"),
    path('api/token/', CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('notes/', Notesview.as_view(), name="notes" ),
    path(r'swagger-docs/', schema_view)
]