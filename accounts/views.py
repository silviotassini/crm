from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request, 'accounts/dashboard.html')

def products(request):
    products_list = Products.objects.all()
    return render(request, 'accounts/products.html', {'products_list':products_list})

def customer(request):
    return render(request, 'accounts/customer.html')