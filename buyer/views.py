from django.shortcuts import render,redirect
from buyer.models import*
from seller.models import*
from site_admin.models import*
from django.contrib import messages
import datetime
# Create your views here.
def register(request):
    return render(request,"BuyerRegister.html")
def registerAction(request):
    name=request.POST["name"]
    gender=request.POST["gender"]
    age=request.POST["age"]
    dob=request.POST["date"]
    country=request.POST["country"]
    phone=request.POST["phone"]
    username=request.POST["username"]
    password=request.POST["password"]
    user=BuyerRegister_tb(Name=name,Gender=gender,Age=age,DateOfBirth=dob,Country=country,Phone=phone,Username=username,Password=password)
    user.save()
    messages.add_message(request,messages.INFO,"Registration was successfull")
    return redirect('register')

def editprofile(request):
    Buyerid=request.session['buyerId']
    edit=BuyerRegister_tb.objects.filter(id=Buyerid)
    return render(request,"edit.html",{'ed':edit})
def editAction(request):
    id=request.session['buyerId']
    name=request.POST["name"]
    gender=request.POST["gender"]
    age=request.POST["age"]
    dob=request.POST["date"]
    country=request.POST['country']
    phone=request.POST["phone"]
    username=request.POST["username"]
    password=request.POST["password"]
    user=BuyerRegister_tb.objects.filter(id=id).update(Name=name,Gender=gender,Age=age,DateOfBirth=dob,Country=country,Phone=phone,Username=username,Password=password)
    return redirect('register')

def products(request):
    pro=Product_tb.objects.all()
    return render(request,"viewproduct.html",{'vi':pro})

def addcart(request,id):
    products=Product_tb.objects.filter(id=id)
    return render(request,"cart.html",{'ca':products})
def cartAction(request):
    productid=request.POST['id']
    buyerid=request.session['buyerId']
    address=request.POST['address']
    phone=request.POST['phn']
    quandity=request.POST['quantity']
    total=request.POST['total']
    stock=request.POST['stock']
    if int(quandity)<int(stock):
        user=Cart_tb(ProductId_id=productid,BuyerId_id=buyerid,ShippingAddress=address,Phone=phone,Quantity=quandity,Total=total)
        user.save()
        messages.add_message(request,messages.INFO,'your product is added to cart')
    else:
        messages.add_message(request,messages.INFO,'Try with Less quantity')
    return redirect('products')

def cartview(request):
    buyerid=request.session['buyerId']
    cartpro=Cart_tb.objects.filter(BuyerId_id=buyerid)
    if len(cartpro) != 0:
        return render(request,'cartview.html',{'cart':cartpro})
    else:
        messages.add_message(request,messages.INFO,"Your Cart is Empty ,select product")
        return redirect('products')
def cartviewAction(request): 
    buyerid=request.session['buyerId']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    name=request.POST['name']
    address=request.POST['address']
    phone=request.POST['phone']
    grandtotal=request.POST['total']
    cartitems=request.POST.getlist('checkbox')
    if len(cartitems) != 0:
        order=Orders_tb(Name=name,Address=address,Phone=phone,BuyerId_id=buyerid,OrderDate=date,OrderTime=time,Grand_Total=grandtotal)
        order.save()    
        for cid in cartitems:
            cartitem=Cart_tb.objects.filter(id=cid)
            quantity=cartitem[0].Quantity
            stock=cartitem[0].ProductId.Stock
            productid=cartitem[0].ProductId
            userid=request.session['buyerId']
            totalprice=cartitem[0].Total   
            newstock=int(stock)-quantity
            product=Product_tb.objects.filter(id=productid.id).update(Stock=newstock)
            cartitem.delete()               
            r=OrdersItem_tb(OrderId_id=order.id,ProductId=productid,BuyerId_id=userid,Quantity=quantity,Total=totalprice)
            r.save() 
        return redirect('paynow',order.id)      
    else:
        messages.add_message(request,messages.INFO,'SELECT ATLEAST ONE ITEM')
    return redirect('cartview')

def paynow(request,id):
    order=OrdersItem_tb.objects.filter(OrderId_id=id)
    return render(request,'Paymentgate.html',{'order':order})
def paymentAction(request):
    buyer_id=request.session['buyerId']
    orderid=request.POST['id'] 
    cardname=request.POST['Card_name']
    cardnumber=request.POST['CardNumber']
    Cvv=request.POST['Cvv']
    Exp_Date=request.POST['Exp_Date']
    payment=Payment_Tb(Card_Name=cardname,Card_Number=cardnumber,BuyerId_id=buyer_id,Order_Id_id=orderid,Cvv=Cvv,Exp_Date=Exp_Date)
    payment.save()
    messages.add_message(request,messages.INFO,"Payment is succesfull")
    return redirect('orderitems')

def orderitems(request):
    order=Orders_tb.objects.filter(BuyerId=request.session['buyerId'])
    orderitem=OrdersItem_tb.objects.filter(OrderId_id=order[0].id).select_related('OrderId').values('OrderId_id')
    return render(request,'orderview.html',{'or':order})
def orderviewAction(request,id):
     orderitem=OrdersItem_tb.objects.filter(OrderId=id,BuyerId_id=request.session['buyerId']).select_related('OrderId')
     order=Orders_tb.objects.filter(id=id)
     return render(request,"OrderProduct.html",{'or':orderitem,'o':order})
def cancelOrder(request,id):
    dlt=Orders_tb.objects.filter(id=id).update(Status="Cancelled")
    return redirect('orderitems')

def viewtracking(request,id):
    tracking=Tracking_tb.objects.filter(OrderId_id=id)
    if len(tracking) != 0:
        return render(request,'trakingDetails.html',{'tr':tracking})            
    else:
        messages.add_message(request,messages.INFO,"No tracking details to view")          
    return redirect('orderitems')

def searchAction(request):
    name=request.POST['search']
    product=Product_tb.objects.filter(Name__istartswith=name) | Product_tb.objects.filter(Price=name)
    return render(request,"viewproduct.html",{'vi':product})
#def searchCategoryAction(request):
    #categoryName=request.POST['Category']
    #price=request.POST['search']
    #product=Product_tb.objects.filter(CategoryId=categoryName,Price__lte=price)
    #return render(request,"viewproduct.html",{'vi':product})

def forgotpassword(request):
    return render(request,'forgotpassword.html')
def forgotpasswordActoin(request):
    username=request.POST['username']
    seller=SellerRegister_tb.objects.filter(Username=username)
    buyer=BuyerRegister_tb.objects.filter(Username=username)
    if seller.count()>0:
        return render(request,'newpassword.html',{'data':username})
    elif buyer.count()>0:
        return render(request,'newpassword.html',{'data':username})
    else:
        messages.add_message(request,messages.INFO,'User does not exist')
        return render(request,'index.html')
def newPasswordAction(request):
    username=request.POST['username']
    name=request.POST['name']
    country=request.POST['country']
    dob=request.POST['dob']
    seller=SellerRegister_tb.objects.filter(Name=name,Country=country,DateOfBirth=dob)
    buyer=BuyerRegister_tb.objects.filter(Name=name,Country=country,DateOfBirth=dob)
    if seller.count()>0:
        return render(request,'enternewpassword.html',{'data':username})
    elif buyer.count()>0:
        return render(request,'enternewpassword.html',{'data':username})
    else:
        messages.add_message(request,messages.INFO,'User does not exist')
        return render(request,'index.html')
def updatepasswordAction(request):
    username=request.POST['username']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    if(newpassword==confirmpassword):
        seller=SellerRegister_tb.objects.filter(Username=username)
        buyer=BuyerRegister_tb.objects.filter(Username=username)
        if seller.count()>0:
            sellerid=seller[0].id
            SellerRegister_tb.objects.filter(id=sellerid).update(Password=newpassword)
            messages.add_message(request,messages.INFO,'Password updated succsesfully')
            return redirect('index')
        elif buyer.count()>0:
            buyerid=buyer[0].id
            BuyerRegister_tb.objects.filter(id=buyerid).update(Password=newpassword)
            messages.add_message(request,messages.INFO,'Password updated succesfully')
            return redirect('index')
        else:
             return redirect('index')
    else:
            messages.add_message(request,messages.INFO,'Password mismatch')
            return render(request,'enternewpassword.html',{'data':username})

def changepassword(request):
    buyerid=request.session['buyerId']
    buyer=BuyerRegister_tb.objects.filter(id=buyerid)
    return render(request,'changepassword.html')

def changepasswordAction(request):
    buyerid=request.session['buyerId']
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    buyer=BuyerRegister_tb.objects.filter(Password=oldpassword,id=buyerid)
    if buyer.count()>0:
        if newpassword==confirmpassword:
            BuyerRegister_tb.objects.filter(id=buyerid).update(Password=newpassword)
            messages.add_message(request,messages.INFO,'password updated sucessfully')
            return redirect('index')
        else:
            messages.add_message(request,messages.INFO,'password not equal')
    else:
        messages.add_message(request,messages.INFO,'password is incorrect')
        return redirect('changepassword')
