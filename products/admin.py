from django.contrib import admin
from .models import *
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name", "image_name", "type", "description", "price"]
class OrderAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "status", "date_created"]
admin.site.register(Products, ProductsAdmin)
admin.site.register(Order, OrderAdmin)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
admin.site.register(AboutUs, AboutUsAdmin)
