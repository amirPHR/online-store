from django.contrib import admin
from .models import Products 
from .models import Comment

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'description' , 'category' , 'price' , 'created_at']
    list_display_links = ['name'] 
    list_editable = ['price' , 'description']
    list_filter = ['created_at']
    list_per_page = 10 
    ordering = ['name']
    search_fields = ['name' , 'category' , 'price']
    
@admin.register(Comment) 
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment' , 'product' , 'user' , 'created_at']
    list_display_links = ['user'] 
    list_editable = ['comment'] 
    list_filter = ['created_at'] 
    list_per_page = 10 
    ordering = ['comment']
    search_fields = ['comment' , 'product' , 'user' , 'created_at']