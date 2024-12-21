from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email' , 'first_name' , 'last_name' , 'phone_number' , 'job' , 'national_code']
    list_display_links = ['username'] 
    list_editable = ['email']
    list_filter = ['date_joined']
    list_per_page = 10 
    ordering = ['username' , 'date_joined']
    search_fields = ['email' , 'first_name' , 'last_name' , 'phone_number', 'national_code']