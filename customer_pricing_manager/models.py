from django.db import models
from customer_manager import models as customer_models
from item_manager import models as item_models

# Create your models here.
class Customer_Pricing(models.Model):
    id=models.DecimalField(max_digits=1000000000, decimal_places=0, primary_key=True)
    customer_id = models.ForeignKey(customer_models.Customer, on_delete=models.CASCADE)
    item_id = models.ForeignKey(item_models.Item, on_delete=models.CASCADE)
    customer_pricing = models.CharField(max_length=60)

