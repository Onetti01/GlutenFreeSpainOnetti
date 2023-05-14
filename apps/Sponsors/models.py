from django.db import models

class Sponsors(models.Model):
    CIF = models.TextField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.TextField()
    email = models.EmailField()

    class Meta:
        db_table = 'Sponsors'
