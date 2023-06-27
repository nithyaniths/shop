from django.db import models

# Create your models here.
class BuyerRegister_tb(models.Model):
    Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    Age=models.CharField(max_length=20)
    DateOfBirth=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

class Cart_tb(models.Model):
    ProductId=models.ForeignKey('seller.Product_tb',on_delete=models.CASCADE)
    BuyerId=models.ForeignKey(BuyerRegister_tb,on_delete=models.CASCADE)
    ShippingAddress=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20)
    Quantity=models.IntegerField()
    Total=models.IntegerField()
class Orders_tb(models.Model):
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20)
    BuyerId=models.ForeignKey(BuyerRegister_tb,on_delete=models.CASCADE)
    Status=models.CharField(max_length=20,default="Pending")
    OrderDate=models.CharField(max_length=20)
    OrderTime=models.CharField(max_length=20)
    Grand_Total=models.IntegerField(default=0)
    
class OrdersItem_tb(models.Model):
    OrderId=models.ForeignKey(Orders_tb,on_delete=models.CASCADE)
    ProductId=models.ForeignKey('seller.Product_tb',on_delete=models.CASCADE)
    BuyerId=models.ForeignKey(BuyerRegister_tb,on_delete=models.CASCADE)
    Quantity=models.IntegerField()
    Total=models.IntegerField()

class Payment_Tb(models.Model):
    BuyerId=models.ForeignKey(BuyerRegister_tb,on_delete=models.CASCADE)
    Order_Id=models.ForeignKey(Orders_tb,on_delete=models.CASCADE)
    Card_Name=models.CharField(max_length=20)
    Card_Number=models.CharField(max_length=20)
    Cvv=models.CharField(max_length=20)
    Exp_Date=models.CharField(max_length=20)
