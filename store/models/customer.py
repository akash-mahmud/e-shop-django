from django.db import models


class Customer(models.Model):
    first_mame=models.CharField(max_length=50)
    last_mame=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password= models.CharField(max_length=500)

    def register(self):
        self.save()