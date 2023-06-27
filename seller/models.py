from django.db import models

# Create your models here.
class SellerRegister_tb(models.Model):
    Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    DateOfBirth=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20)
    File=models.FileField()
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    Status=models.CharField(max_length=20,default="pending")

class Product_tb(models.Model):
    Name=models.CharField(max_length=20)
    File=models.FileField()
    Price=models.CharField(max_length=20)
    Stock=models.IntegerField()
    Details=models.CharField(max_length=20)
    SellerId=models.ForeignKey(SellerRegister_tb,on_delete=models.CASCADE)
    CategoryId=models.ForeignKey('site_admin.category_tb',on_delete=models.CASCADE)

class Tracking_tb(models.Model):
    OrderId=models.ForeignKey('buyer.Orders_tb',on_delete=models.CASCADE)
    Time=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Details=models.CharField(max_length=20)