from django.contrib import admin
from .models import Expenses
# Register your models here.

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('payment_method', 'category', 'item', 'quantity', 'amount', 'date', 'check')
    list_display_links = ('payment_method', )
    search_fields = ('item', 'category', 'payment_method')
    list_filter = ('category', 'payment_method')
    list_per_page = 20


admin.site.register(Expenses, ExpensesAdmin)
