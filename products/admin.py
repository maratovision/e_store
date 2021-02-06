from django.contrib import admin
from .models import *
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name", "image_name", "type", "description", "price"]
admin.site.register(Products, ProductsAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", 'price', "status", "date_created"]
admin.site.register(Order, OrderAdmin)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
admin.site.register(AboutUs, AboutUsAdmin)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'address', 'latitude', 'longtitude', 'type']
admin.site.register(Contacts, ContactsAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','full_name', 'gender', 'birth_date', 'twitter_link']
admin.site.register(Profile, ProfileAdmin)