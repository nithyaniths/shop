from django.shortcuts import render,redirect
from seller.models import*
from site_admin.models import*
from buyer.models import*
from django.contrib import messages
import datetime
# Create your views here.
def sellerRegister(request):
    return render(request,'SellerRegister.html')
def sellerAction(request):
    name=request.POST["name"]
    gender=request.POST["gender"]
    dob=request.POST["date"]
    country=request.POST["country"]
    phone=request.POST["phone"]
    if len(request.FILES)>0:      
       image=request.FILES["file"]
    else:
        image="no pic"
    username=request.POST["username"]
    password=request.POST["password"]
    user=SellerRegister_tb(Name=name,Gender=gender,DateOfBirth=dob,Country=country,Phone=phone,File=image,Username=username,Password=password)
    user.save()
    messages.add_message(request,messages.INFO,"Registration was succesfull")
    return redirect('sellerRegister')
def editseller(request):
    sellerId=request.session['sellerId']
    edit=SellerRegister_tb.objects.filter(id=sellerId)
    return render(request,"editseller.html",{'ed':edit})

def editSellerAction(request):
    id=request.session['sellerId']
    im=SellerRegister_tb.objects.filter(id=id)
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['date']
    country=request.POST['country']
    if len(request.FILES)>0:
        img=request.FILES['file']
    else:
        img=im[0].File
    username=request.POST['username']
    password=request.POST['password']
    user=SellerRegister_tb.objects.filter(id=id).update(Name=name,Gender=gender,DateOfBirth=dob,Country=country,Username=username,Password=password)
    seller_object=SellerRegister_tb.objects.get(id=id)
    seller_object.File=img
    seller_object.save()
    return redirect('sellerRegister')

def addproduct(request):
    category=category_tb.objects.all()
    return render(request,"addproduct.html",{'ca':category})
def addproductAction(request):
    name=request.POST['name']
    if len(request.FILES)>0:
        image=request.FILES['file']
    else:
        image="no pic"
    price=request.POST['price']
    stock=request.POST['stock']
    details=request.POST['details']
    sellerid=request.session['sellerId']   
    category=request.POST['category']
    user=Product_tb(Name=name,File=image,Price=price,Stock=stock,Details=details,SellerId_id=sellerid,CategoryId_id=category)
    user.save()
    return redirect('addproduct')

def productview(request):  
    product=Product_tb.objects.filter(SellerId_id=request.session['sellerId'])
    return render(request,"productview.html",{'vi':product})

def editproduct(request,id):
    category=category_tb.objects.all()
    edit=Product_tb.objects.filter(id=id)
    return render(request,"editproduct.html",{'ed':edit,'ca':category})
def edProductAction(request):   
    id=request.POST['id']
    sellerid=request.session['sellerId']
    name=request.POST['name']
    im=Product_tb.objects.filter(id=id)
    if len(request.FILES)>0:
        image=request.FILES['file']
    else:
        image=im[0].File  
    price=request.POST['price']
    stock=request.POST['stock']
    details=request.POST['details']
    category=request.POST['category']  
    user=Product_tb.objects.filter(id=id).update(Name=name,Price=price,Stock=stock,Details=details,CategoryId_id=category,SellerId_id=sellerid)
    image_upload=Product_tb.objects.get(id=id)
    image_upload.File=image
    image_upload.save()
    return redirect('productview')

def deleteproduct(request,id):
    dlt=Product_tb.objects.filter(id=id).delete()
    return redirect('productview')

def orderDetails(request):
    sellerProduct=Product_tb.objects.filter(SellerId_id=request.session['sellerId']).values('id')
    orderitem=OrdersItem_tb.objects.filter(ProductId_id__in=sellerProduct).select_related('OrderId').values('OrderId_id')
    orders=Orders_tb.objects.filter(id__in=orderitem)
    return render(request,'orderDetails.html',{'or':orders})
def orderDetailsAction(request,id):
    sellerProduct=Product_tb.objects.filter(SellerId_id=request.session['sellerId']).values('id')
    orderitem=OrdersItem_tb.objects.filter(OrderId=id,ProductId_id__in=sellerProduct).select_related('OrderId')
    order=Orders_tb.objects.filter(id=id)
    return render(request,'ProductDetails.html',{'or':order,'o':orderitem})
    
def OrderApprove(request,id):
    order=Orders_tb.objects.filter(id=id).update(Status="Approved")
    return redirect('orderDetails')

def OrderReject(request,id):  
    neworder=Orders_tb.objects.filter(id=id).update(Status="Rejected")
    return redirect('orderDetails')
def confirmCancel(request,id):
    orderitem=OrdersItem_tb.objects.filter(OrderId_id=id)
    for v in orderitem:
        pro=Product_tb.objects.filter(id=v.ProductId_id)
        quantity=v.Quantity
        stock=pro[0].Stock
        newstock=stock+quantity
        product=Product_tb.objects.filter(id=v.ProductId_id).update(Stock=newstock)
    neworder=Orders_tb.objects.filter(id=id).update(Status="Cancelled")
    return redirect('productview')

def trackingdetails(request,id):
    details=Orders_tb.objects.filter(id=id)
    return render(request,'tracking.html',{'de':details})

def trackingAction(request):
    id=request.POST['id']
    orderid=Orders_tb.objects.get(id=id)
    details=request.POST['details']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    tracking=Tracking_tb(OrderId=orderid,Time=time,Date=date,Details=details)
    tracking.save()
    return redirect('orderDetails')