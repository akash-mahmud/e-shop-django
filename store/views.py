from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
def index(request):
   products = None
   categories = Category.get_all_categories()
   categoryId = request.GET.get('category')
   if categoryId:
      products = Product.get_all_products_by_category(categoryId)
   else:
      products = Product.get_all_products()
   context = {'products':products  , 'categories':categories}

   return render(request, 'index.html' , context)
