from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.model.customer import Customer
from django.views import View
from store.model.product import Product
from store.model.orders import Order
from store.middleware.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})