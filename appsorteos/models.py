from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Sorteo(models.Model):
    fecha = models.DateField()
    valor_papeleta = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    def __str__(self):
        return f"Sorteo del {self.fecha}"
