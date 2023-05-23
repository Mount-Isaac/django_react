import json 
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view



from .models import Product 
from .serializers import ProductSeriliazer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
	"""
	DRF API View
	"""    
	try:
		serializer = ProductSeriliazer(data=request.data)
		if serializer.is_valid():
			print(serializer.data)
			data = serializer.data
			return Response(data)
	except Exception as e:
		# print(dir(serializer))
		# print(e)
		pass
		
	# instance = Product.objects.all().order_by("?").first()
	# data = {}
	# if instance:
	# 	data = ProductSeriliazer(instance).data
	# return data


	# model_data = Product.objects.all().order_by("?").first()
	# if model_data:
	# 	data = model_to_dict(model_data)
		# data['id'] = model_data.id
		# data['title'] = model_data.title
		# data['content'] = model_data.content
		# data['price'] = model_data.price
	# return JsonResponse(data)
	  