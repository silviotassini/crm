from django.contrib import admin

# Register your models here.
from .models import Customer,Products, Order

admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)