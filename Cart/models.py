from django.db import models
from Users.models import CustomUser 
from Products.models import Products 

class Cart(models.Model):
    user = models.ForeignKey(CustomUser , on_delete = models.CASCADE) 
    product = models.ForeignKey(Products , on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0 , blank=True)
    
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price
        super().save(*args, **kwargs)