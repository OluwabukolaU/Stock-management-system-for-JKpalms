from django.contrib import admin
from .forms import StockCreateForm

from .models import Stock

# Register your models here.

#to show/customize the fields in the admin panel

class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity', 'price', 'order_date']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name']

admin.site.register(Stock, StockCreateAdmin)
