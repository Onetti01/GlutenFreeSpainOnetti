from django.db import models

# Create your models here.


class suscriptionTypes(models.Model):
    class Meta:
        verbose_name = 'suscriptionTypes'
        verbose_name_plural = 'suscriptionTypes'

    # columnas
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name
