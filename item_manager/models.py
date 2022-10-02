from ctypes.wintypes import CHAR
from django.db import models

# Create your models here.
class Item(models.Model):
    id=models.DecimalField(max_digits=1000000000, decimal_places=0, primary_key=True)
    number=models.CharField(max_length=60)
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=60)
    item_cost_internal=models.CharField(max_length=60)
    # item_cost_internal=models.DecimalField(max_digits=10, decimal_places=2)
