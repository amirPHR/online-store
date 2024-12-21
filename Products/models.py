from django.db import models
from category.models import Category
from Users.models import CustomUser

class Products(models.Model):
    name = models.CharField(max_length = 255) 
    description = models.TextField()
    category = models.ForeignKey(Category , on_delete = models.CASCADE) 
    price = models.PositiveIntegerField() 
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateField(auto_now_add = True)
    
class Comment(models.Model):
    user = models.ForeignKey(CustomUser , on_delete = models.CASCADE) 
    product = models.ForeignKey(Products , on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)