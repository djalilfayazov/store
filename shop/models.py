from django.db import models
from ckeditor import fields
from django.contrib.auth.models import User


class Product(models.Model):
	item_title = models.CharField('Title', max_length=500)
	item_img = models.CharField('IMG', max_length=5000)
	item_body = fields.RichTextField('Body')

	item_price = models.FloatField('Price', default=10.0)

	item_date = models.DateField('Date')
	isdigital = models.BooleanField('Digital', default=False)


	def __str__(self):
		return f'{self.item_title}'

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'


