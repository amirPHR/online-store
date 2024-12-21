from django.contrib import admin
from .models import Payment

@admin.register(Payment) 
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user' , 'order' , 'status' , 'payment_date']
    list_display_links = ['user']
    list_editable = ['status']
    list_filter = ['status'] 
    list_per_page = 10 
    ordering = ['user' , 'payment_date']
    search_fields = ['user' , 'order' , 'status' , 'payment_date']