from django.contrib import admin
from .models import Cart 

@admin.register(Cart) 
class CartAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'quantity' , 'total_price'] 
    list_display_links = ['user']
    search_fields = ['user' , 'product' , 'quantity']