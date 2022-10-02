from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.DecimalField(max_digits=1000000000, decimal_places=0, primary_key=True)
    name=models.CharField(max_length=60)
    address=models.CharField(max_length=60)
    city=models.CharField(max_length=60)
    state=models.CharField(max_length=60)
    country=models.CharField(max_length=60)
    zip_code=models.CharField(max_length=10)