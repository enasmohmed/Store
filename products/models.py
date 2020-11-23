from django.db import models

# Create your models here.
from django.urls import reverse
import datetime

class Product(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True)
    price = models.PositiveIntegerField()
    sale = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('product_details', args=(self.id, ))

    def __str__(self):
        return self.title