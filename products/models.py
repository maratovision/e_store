from django.contrib.auth.models import User
from django.db import models
from datetime import date

# Create your models here.

class Products(models.Model):
    type_of_products = (
        ("Laptop", "Laptop"),
        ("PC", "PC"),
        ("Mobile", "Mobile")
    )
    name = models.CharField(max_length=50)
    image_name = models.ImageField(blank=True, null=True, default="default.png")
    description = models.CharField(max_length=200)
    type = models.CharField(choices=type_of_products, max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    statuses = (
        ("In Process", "In Process"),
        ("Delivered", "Delivered"),
        ("Not Delivered", "Not Delivered")
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=statuses, default="In Process")
    date_created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(max_length=20)

    def __str__(self):
        return f"{self.product} {self.quantity}"

class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

class Contacts(models.Model):
    type_contact = (
        ('Phone number', 'Phone number'),
        ('Email', 'Email'),
        ('Physical address', 'Physical address')
    )
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.IntegerField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=type_contact, default='Phone number')
    latitude = models.IntegerField(max_length=20, blank=True, null=True)
    longtitude = models.IntegerField(max_length=20, blank=True, null=True)

class Profile(models.Model):
    genders = (
        ('F', "F"),
        ('M', "M")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_image.png', blank=True)
    full_name = models.CharField(max_length=50)
    gender = models.CharField(choices=genders, max_length=20)
    description = models.TextField()
    birth_date = models.DateField(default=date.today())
    twitter_link = models.CharField(max_length=100)




