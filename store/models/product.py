from django.db import models
from .category import Category
class Product (models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250 , default='')
    image = models.ImageField(upload_to= 'uploads/products/')
   
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category(category_id):
        if category_id:
            return Product.objects.filter(category= category_id)
        else:
            Product.get_all_products()