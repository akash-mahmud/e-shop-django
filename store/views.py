from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
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


def signUp(request):
      if request.method == 'GET':
         
          return render(request, 'signup.html' )
      else:
         formData = request.POST
         first_name = formData.get('firstname')
         last_name = formData.get('lastname')
         email= formData.get('email')
         phone=formData.get('phone')
         password= formData.get('password')
         error_message = None;
         value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
         customer = Customer(first_mame = first_mame , last_mame = last_mame ,email=email ,phone=phone
                             , password= password)
         if (not customer.first_name):
            error_message = "First Name Required !!"
         elif len(customer.first_name) < 4:
               error_message = 'First Name must be 4 char long or more'
         elif not customer.last_name:
               error_message = 'Last Name Required'
         elif len(customer.last_name) < 4:
               error_message = 'Last Name must be 4 char long or more'
         elif not customer.phone:
               error_message = 'Phone Number required'
         elif len(customer.phone) < 10:
               error_message = 'Phone Number must be 10 char Long'
         elif len(customer.password) < 6:
               error_message = 'Password must be 6 char long'
         elif len(customer.email) < 5:
               error_message = 'Email must be 5 char long'
         elif customer.isExists():
               error_message = 'Email Address Already Registered..'
               
               
        
         if not error_message:
            print(first_name, last_name, phone, email, password)
            # customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
         else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)