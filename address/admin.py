from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user' , 'country' , 'city' , 'address']
    list_display_links = ['user']
    list_editable = ['country' , 'city' , 'address']
    list_filter = ['country' , 'city' , 'address']
    list_per_page = 10 
    ordering = ['country' , 'city' , 'address']
    search_fields = ['user' , 'country' , 'city' , 'address']