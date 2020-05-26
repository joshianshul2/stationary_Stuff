from django.db import models

# Create your models here.
from django.db.models import CharField


class User(models.Model):
    count = 0
    name = models.CharField(max_length=128 , unique=False)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=128,default='aj')
    message=models.TextField(max_length=128,default='Anji')


class Cart(models.Model):
    name = models.CharField(max_length=128, unique=False)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=128, default='aj')
    message = models.TextField(max_length=128, default='Anji')


