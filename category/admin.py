from django.contrib import admin
from .models import Category

@admin.register(Category) 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' , 'description' , 'is_active'] 
    list_display_links = ['name'] 
    list_editable = ['is_active'] 
    list_filter = ['created_at'] 
    list_per_page = 10 
    ordering = ['name']
    search_fields = ['name' , 'description' , 'is_active']