from django.contrib import admin
from .models import Comment 
from Products.models import Products 

@admin.register(Comment) 
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment' , 'product' , 'user' , 'created_at']
    list_display_links = ['user'] 
    list_editable = ['comment'] 
    list_filter = ['created_at'] 
    list_per_page = 10 
    ordering = ['comment']
    search_fields = ['comment' , 'product' , 'user' , 'created_at']