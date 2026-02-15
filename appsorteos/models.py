import datetime
from django.db import models

from appgeneral.models import TimeStampedModel

# Create your models here.


class Sorteo(TimeStampedModel):
    fecha = models.DateField()
    valor_papeleta = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    def __str__(self):
        return f"Sorteo del {self.fecha}"
