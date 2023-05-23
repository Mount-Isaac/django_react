from django.urls import path
from .views import  class_api_call

urlpatterns = [
    path('', class_api_call.as_view() )
]