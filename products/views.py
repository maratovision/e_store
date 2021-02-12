from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .models import *
from .forms import OrderForm, ProfileForm, SignupForm


# Create your views here.
from .tokens import account_activation_token


def products_page(request):
    products = Products.objects.all() # SELECT * FROM PRODUCTS
    return render(request, 'product/main.html', {"products":products})

def order_page(request, product_id):
    try:
        profile = Profile.objects.get(user = request.user)
        product = Products.objects.get(id = product_id)
        total_price = 0
        form = OrderForm(initial={'product':product, 'user': request.user})
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                total_price = product.price * form.cleaned_data['quantity']
                if product.sale:
                    total_price = total_price - total_price * 0.2
                form.save()
                profile.order_count += 1
                profile.save()
                # return redirect('products')
        return render(request, 'product/order.html', {'form':form, 'total_price':total_price})
    except Products.DoesNotExist:
        return HttpResponse('Not found')

def register_page(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('product/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    return render(request, 'product/register.html', {'form': form})

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
    order_user = request.user
    orders = order_user.order_set.all()
    form = ProfileForm(instance=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES ,instance=user)
        if form.is_valid():
            form.save()
    context = {'form':form, 'orders':orders}
    return render(request, 'product/profile.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')