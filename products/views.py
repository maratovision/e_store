from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm

# Create your views here.
def products_page(request):
    products = Products.objects.all() # SELECT * FROM PRODUCTS
    return render(request, 'product/main.html', {"products":products})

def order_page(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'product/order.html', {'form':form})

def register_page(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'product/register.html', {'form':form})

def user_list(request):
    user = User.objects.all()
    context = {'user':user}
    return render(request, 'product/user.html', context)

def about_us(request):
    about = AboutUs.objects.all()
    context = {'about':about}
    return render(request, 'product/about_us.html', context)
