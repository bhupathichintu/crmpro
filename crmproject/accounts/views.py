from django.shortcuts import render
from .models import Customers,Products,Orders
def home(request):
    customers = Customers.objects.all()
    products = Products.objects.all()
    orders =  Orders.objects.all()
    total_orders = len(orders)
    delivery_orders = orders.filter(status='Delivered').count()
    pending_orders = orders.filter(status='Pending ').count()
    outfordelivery_orders = orders.filter(status='Outfordelivery').count()

    context = {
        'customers':customers,
        'orders':orders,
        'products':products,
        'total_orders':total_orders,
        'delivery_orders':delivery_orders,
        'pending_orders':pending_orders,
        'outfordelivery_orders':outfordelivery_orders
    }

    return render(request, 'accounts/dashboard.html',context)

def products(request):
    return render(request, 'accounts/products.html')

def orders(request):
    return render(request, 'accounts/orders.html')
