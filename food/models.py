from django.db import models

# Create your models here.

class user(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    class Meta:
        db_table='user'

class customer(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    class Meta:
        db_table='customer'

