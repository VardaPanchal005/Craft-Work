from django.contrib import admin
from .model.product import Product
from .model.customer import Customer
from .model.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Customer )
admin.site.register(Order )