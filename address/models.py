from django.db import models
from Users.models import CustomUser 

class Address(models.Model):
    user = models.ForeignKey(CustomUser , on_delete = models.CASCADE) 
    country = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    address = models.TextField()
    
    def __str__(self):
        return self.user.username