
from django.urls import path
from . import  views

urlpatterns = [
    path("",views.index,name="index"),
    path("cart",views.cart,name="cart.html"),
    path("dsa",views.dsa,name='dsa.html'),
    path("thankyou",views.thankyou,name='thankyou.html')


]