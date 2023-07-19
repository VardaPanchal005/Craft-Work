from django.views import View
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import admin
from django.contrib.auth.hashers import check_password
from django.views import View
from store.model.product import Product

class cart(View):
    def get(self,request):
       ids=list(request.session.get('cart').keys())
       product=Product.get_products_by_id(ids)
       print(product)

       return render(request,'cart.html',{'cart':product})
   
        




