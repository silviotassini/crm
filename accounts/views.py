from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

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

def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
       # print("printing : ", request.POST)
       form = OrderForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
       # print("printing : ", request.POST)
       form = OrderForm(request.POST, instance=order)
       if form.is_valid():
           form.save()
           return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)