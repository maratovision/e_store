from django.urls import path
from .views import products_page, order_page, register_page, user_list, about_us

urlpatterns = [
    path('', products_page, name='products'),
    path('order/', order_page),
    path('register/', register_page),
    path('user/', user_list),
    path('about_us', about_us)
]