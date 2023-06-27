from django.shortcuts import render,redirect
from site_admin.models import*
from buyer.models import*
from seller.models import*
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")
def loginAction(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=admin_tb.objects.filter(Username=username,Password=password)
    buyer=BuyerRegister_tb.objects.filter(Username=username,Password=password)
    seller=SellerRegister_tb.objects.filter(Username=username,Password=password)
    if user.count()>0:
        request.session['id']=user[0].id       
        return render(request,"AdminHome.html")  
    elif buyer.count()>0:
        request.session['buyerId']=buyer[0].id
        return render(request,"BuyerHome.html")             
                      
    elif seller.count()>0:        
         if(seller[0].Status=="Approved"):
            request.session['sellerId']=seller[0].id
            return render(request,"SellerHome.html")                  
         else:
            messages.add_message(request,messages.INFO,'Please wait for approval')
            return redirect('login')
    else:
       messages.add_message(request,messages.INFO,'Invalid username or password')
       return redirect('login')  
def viewseller(request):
    user=SellerRegister_tb.objects.all()
    return render(request,"viewseller.html",{'us':user})     
def approved(request,id):
    d=SellerRegister_tb.objects.filter(id=id).update(Status="Approved")
    return redirect('viewseller')
def reject(request,id):
    r=SellerRegister_tb.objects.filter(id=id).update(Status="Rejected")
    return redirect('viewseller')

def addcategory(request):
    return render(request,'addcategory.html')
def categoryAction(request):
    name=request.POST['name']
    user=category_tb(CategoryName=name)
    user.save()
    return redirect('addcategory')
def logout(request):
    request.session.flush()
    return redirect('index')

