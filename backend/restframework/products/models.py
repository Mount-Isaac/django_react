from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField(blank=True, null=True)
	price = models.DecimalField(max_digits=15, decimal_places = 2, default=99.99)

	#setter methods for price & discount respectively
	@property
	def sale_price(self):
		return round(float(self.price) * 0.9, 2)

	@property
	def get_discount(self):
		return round(float(self.price) * 0.1, 2)