from django.contrib import admin

# Register your models here.
from .models import Customer,Products, Order, Tag

admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Tag)
admin.site.register(Order)