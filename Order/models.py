from django.db import models
from Users.models import CustomUser 
from Products.models import Products 
from Cart.models import Cart 
from address.models import address

class Order(models.Model):
    user = models.ForeignKey(CustomUser , on_delete = models.CASCADE) 
    
    STATUS_CHOICES = [
        ('received ' , 'Recived'),
        ('did_not_receive' , 'Did not receive')
    ]
    status = models.CharField(max_length = 20 , choices = STATUS_CHOICES) 
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE) 
    address = models.ForeignKey(address , on_delete = models.CASCADE) 