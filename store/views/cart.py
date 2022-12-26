from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.model.customer import Customer
from django.views import  View
from store.model.product import  Product
class cart(View):
    def get(self,request):
       ids=list(request.session.get('cart').keys())
       print(ids)
       products=Product.get_products_by_id(ids)
       print(products)
       data = {}
       data['products'] = products
       return render(request,'cart.html',data)
   
        




