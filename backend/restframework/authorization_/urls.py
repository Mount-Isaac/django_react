from django.urls import path
from .views import login_class_APIView

urlpatterns = [
    path('', login_class_APIView.as_view(), name='login')
]