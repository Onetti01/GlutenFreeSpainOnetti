from django.db import models
from ..Categories.models import Categories


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    is_vegetarian = models.BooleanField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.TextField()

    class Meta:
        db_table = 'Products'