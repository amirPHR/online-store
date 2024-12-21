from django.contrib import admin
from .models import Order

@admin.register(Order) 
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user' , 'status' , 'cart' , 'address']
    list_display_links = ['user']
    list_editable = ['status']
    list_filter = ['status']
    list_per_page = 10 
    ordering = ['status']
    search_fields = ['user' , 'status' , 'cart' , 'address']