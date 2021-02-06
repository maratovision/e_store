from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, ProfileForm

# Create your views here.
def products_page(request):
    products = Products.objects.all() # SELECT * FROM PRODUCTS
    return render(request, 'product/main.html', {"products":products})

def order_page(request, product_id):
    try:
        product = Products.objects.get(id = product_id)
        form = OrderForm(initial={'product':product})
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('products')
        return render(request, 'product/order.html', {'form':form})
    except Products.DoesNotExist:
        return HttpResponse('Not found')

def register_page(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user = user)
            return redirect('/')
    return render(request, 'product/register.html', {'form':form})

def user_list(request, user_id):
    user = User.objects.get(id = user_id)
    orders = user.order_set.all()
    context = {'user': user, 'orders': orders}
    return render(request, 'product/user.html', context)

def about_us(request):
    about = AboutUs.objects.all()
    context = {'about': about}
    return render(request, 'product/about_us.html', context)

def contacts(request):
    contacts = Contacts.objects.all()
    context = {'contacts':contacts}
    return render (request, 'product/contacts.html', context)

def update_order(request, order_id):
    order = Order.objects.get(id = order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'product/order.html', {'form': form})

def delete_order(request, order_id):
    order = Order.objects.get(id = order_id)
    order.delete()
    return redirect('products')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        login(request, user)
        return redirect('products')

    return render(request, 'product/login.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def account_settings(request):
    user = request.user.profile
    form = ProfileForm(instance=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES ,instance=user)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'product/profile.html', context)
