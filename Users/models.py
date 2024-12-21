from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length = 20 , unique = True) 
    job = models.CharField(max_length = 225) 
    national_code = models.CharField(max_length = 10 , unique = True)