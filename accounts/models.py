from sre_constants import CATEGORY
from sre_parse import CATEGORIES
from telnetlib import STATUS
from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_Created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    CATEGORY = (('in','in'),('out','out'))
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_Created = models.DateTimeField(auto_now_add=True,  null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (('Pendente','Pendente'),
              ('Saiu p entrega', 'Saiu p entrega'),
              ('Entregue','Entregue'))
    #customer = 
    #product = 

    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_Created = models.DateTimeField(auto_now_add=True,  null=True)