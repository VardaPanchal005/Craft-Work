from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='uploads/product/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
