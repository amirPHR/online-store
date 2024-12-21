from django.db import models
from Order.models import Order 
from Cart.models import Cart 
from Users.models import CustomUser

class Payment(models.Model):
    user = models.ForeignKey(CustomUser , on_delete = models.CASCADE)    
    order = models.ForeignKey(Order , on_delete = models.CASCADE) 
    price = models.ForeignKey(Cart , on_delete = models.CASCADE) 
    
    STATUS_CHOICES = [
        ('paid' , 'Paid') , 
        ('not_paid' , 'Not Paid')
    ]
    
    status = models.CharField(max_length = 20 , choices=STATUS_CHOICES) 
    payment_date = models.DateField(auto_now_add = True)    