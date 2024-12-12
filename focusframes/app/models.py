from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    Category_name=models.TextField()

class product(models.Model):
    pid=models.TextField()
    name=models.TextField()
    dis=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img = models.FileField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
   

