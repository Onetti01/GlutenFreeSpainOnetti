from django.db import models
from ..Sponsors.models import Sponsors
from ..suscriptionTypes.models import suscriptionTypes

class Bills(models.Model):
    is_paid = models.BooleanField()
    CIF_sponsor = models.ForeignKey(Sponsors, on_delete=models.CASCADE)
    pdf = models.TextField()
    suscription = models.ForeignKey(suscriptionTypes, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Bills'