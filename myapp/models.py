from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 15,decimal_places=2)
    description = models.TextField()
# Create your models here.
