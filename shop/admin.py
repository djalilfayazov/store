from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'item_title', 'item_price')
	list_display_links = ('item_title',)
	ordering = ('item_price',)

