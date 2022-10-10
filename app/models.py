from datetime import datetime
from email.policy import default
from time import timezone
from django.db import models

# Create your models here.


class Seller(models.Model):
    name = models.CharField(max_length=255,default='Michael Dsouza')
    address = models.TextField(default='Shop No.1, Rosy Apartment, Cabin Road, Bhayander(west), Mumbai-401106')
    phone = models.IntegerField(default = '+91 9876543210')
    date = models.DateField(default=datetime.today())

class Buyer(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.IntegerField()
    purchased_date = models.DateTimeField(default =datetime.now())

    def __str__(self):
        return self.name

class Product(models.Model):
    prod_img = models.ImageField(upload_to='media/')
    prod_name = models.CharField(max_length=255)
    prod_desc = models.TextField()
    prod_price = models.IntegerField()
    prod_ratings = models.IntegerField()

    def __str__(self) :
        return self.prod_name