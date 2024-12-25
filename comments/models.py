from django.db import models
from Users.models import CustomUser 
from Products.models import Products 

class Comment(models.Model):
    user = models.ForeignKey(CustomUser , on_delete = models.CASCADE) 
    product = models.ForeignKey(Products , on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)