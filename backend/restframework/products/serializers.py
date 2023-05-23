from rest_framework import serializers
from .models import Product

class ProductSeriliazer(serializers.ModelSerializer):
    Discount = serializers.SerializerMethodField(read_only=True)
    Price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'content',
            'Price',
            'Discount'
        ]
    # when the field name != respective matching model name
    # then we declare a method with the declared variable name
    # prefixed by keyword get which returns the value from the
    # from the object setter method
    # ||===|| get_variable(self, obj)
    def get_Price(self, obj):
        try:
            return obj.sale_price
        except:
            return None
    
    def get_Discount(self, obj):
        try:
            return obj.get_discount
        except:
            return None