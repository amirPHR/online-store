from django.contrib import admin
from .models import Products 

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'description' , 'category' , 'price' , 'created_at']
    list_display_links = ['name'] 
    list_editable = ['price' , 'description']
    list_filter = ['created_at']
    list_per_page = 10 
    ordering = ['name']
    search_fields = ['name' , 'category' , 'price']
    
