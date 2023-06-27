"""
URL configuration for online_shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from site_admin import views as adminview
from buyer import views as buyerview
from seller import views as sellerview
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name="index"),
    path('login/',adminview.login,name="login"),
    path('loginAction/',adminview.loginAction,name="loginAction"),
    path('register/',buyerview.register,name="register"),
    path('registerAction/',buyerview.registerAction,name="registerAction"),
    path('sellerRegister/',sellerview.sellerRegister,name="sellerRegister"),
    path('sellerAction/',sellerview.sellerAction,name="sellerAction"),
    path('editprofile/',buyerview.editprofile,name="editprofile"),
    path('editAction/',buyerview.editAction,name="editAction"),
    path('viewseller/',adminview.viewseller,name="viewseller"),
    path('approved<int:id>/',adminview.approved,name="approved"),
    path('reject<int:id>/',adminview.reject,name="reject"),
    path('editseller/',sellerview.editseller,name="editseller"),
    path('editSellerAction/',sellerview.editSellerAction,name="editSellerAction"),
    path('addcategory/',adminview.addcategory,name="addcategory"),
    path('categoryAction/',adminview.categoryAction,name="categoryAction"),
    path('addproduct/',sellerview.addproduct,name="addproduct"),
    path('addproductAction/',sellerview.addproductAction,name="addproductAction"),
    path('productview/',sellerview.productview,name="productview"),
    path('editproduct<int:id>/',sellerview.editproduct,name="editproduct"),
    path('deleteproduct<int:id>/',sellerview.deleteproduct,name="deleteproduct"),
    path('edProductAction/',sellerview.edProductAction,name="edProductAction"),
    path('products/',buyerview.products,name="products"),
    path('addcart<int:id>/',buyerview.addcart,name="addcart"),
    path('cartAction/',buyerview.cartAction,name="cartAction"),
    path('cartview/',buyerview.cartview,name="cartview"),
    path('cartviewAction/',buyerview.cartviewAction,name="cartviewAction"),
    path('orderitems/',buyerview.orderitems,name="orderitems"),
    path('orderviewAction<int:id>/',buyerview.orderviewAction,name="orderviewAction"),
    path('cancelOrder<int:id>/',buyerview.cancelOrder,name="cancelOrder"),
    path('orderDetails/',sellerview.orderDetails,name="orderDetails"),
    path('orderDetailsAction<int:id>/',sellerview.orderDetailsAction,name="orderDetailsAction"),
    path('OrderApprove<int:id>/',sellerview.OrderApprove,name="OrderApprove"),
    path('OrderReject<int:id>/',sellerview.OrderReject,name="OrderReject"),
    path('trackingdetails<int:id>/',sellerview.trackingdetails,name="trackingdetails"),
    path('trackingAction/',sellerview.trackingAction,name="trackingAction"),
    path('viewtracking<int:id>/',buyerview.viewtracking,name="viewtracking"),
    path('searchAction/',buyerview.searchAction,name="searchAction"),
    path('confirmCancel<int:id>/',sellerview.confirmCancel,name="confirmCancel"),
    path('paynow<int:id>/',buyerview.paynow,name="paynow"),
    path('paymentAction/',buyerview.paymentAction,name="paymentAction"),
    path('forgotpassword/',buyerview.forgotpassword,name="forgotpassword"),
    path('forgotpasswordActoin/',buyerview.forgotpasswordActoin,name="forgotpasswordActoin"),
    path('newPasswordAction/',buyerview.newPasswordAction,name="newPasswordAction"),
    path('updatepasswordAction/',buyerview.updatepasswordAction,name="updatepasswordAction"),
    path('changepassword/',buyerview.changepassword,name="changepassword"),
    path('changepasswordAction/',buyerview.changepasswordAction,name="changepasswordAction"),
    path('logout/',adminview.logout,name="logout")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
