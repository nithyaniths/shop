from django.db import models

# Create your models here.
class admin_tb(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

class category_tb(models.Model):
    CategoryName=models.CharField(max_length=20)