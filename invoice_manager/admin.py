from django.contrib import admin
from .models import Invoice

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number',)

admin.site.register(Invoice, InvoiceAdmin)