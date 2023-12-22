from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('additem',views.additem,name="additem"),
    path('biditem',views.biditem,name="biditem"),
    path('validate',views.validate,name="validate"),
    path('item/biditem',views.biditem,name="biditem"),
    path('prod',views.sub_product,name="sub_product"),
    path('main_prod',views.sub_product_main,name="sub_product_main"),
]