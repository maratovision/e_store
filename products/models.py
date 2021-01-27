from django.db import models

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
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=statuses, default="In Process")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()


