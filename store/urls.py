
from django.contrib import admin
from django.urls import path
from.views import index , signUp
urlpatterns = [
    path('',index),
    path('signup',signUp),

]
