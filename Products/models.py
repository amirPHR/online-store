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