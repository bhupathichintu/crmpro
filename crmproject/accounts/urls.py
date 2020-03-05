from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),

]