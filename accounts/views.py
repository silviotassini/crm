from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    customer_list = Customer.objects.all()
    order_list = Order.objects.all()

    total_orders = order_list.count()
    delivered = order_list.filter(status='Saiu p entrega').count()
    pending = order_list.filter(status='Pendente').count()

    context = {'customer_list':customer_list, 'order_list':order_list,'total_orders':total_orders, 'delivered':delivered,'pending':pending}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products_list = Products.objects.all()
    return render(request, 'accounts/products.html', {'products_list':products_list})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {'customer':customer,'orders':orders,'total_orders':total_orders}
    return render(request, 'accounts/customer.html',context)