from django.contrib import admin
from . models import Customer_Pricing

# Register your models here.
class Customer_PricingAdmin(admin.ModelAdmin):
    list_display = ('customer_id',)

admin.site.register(Customer_Pricing, Customer_PricingAdmin)