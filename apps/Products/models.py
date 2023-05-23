from django.db import models
from ..Categories.models import Categories
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    is_vegetarian = models.BooleanField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
    votaciones = models.IntegerField(default=0)

    class Meta:
        db_table = 'Products'


@receiver(pre_delete, sender=Products)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        file_path = instance.image.path
        if os.path.exists(file_path):
            os.remove(file_path)
