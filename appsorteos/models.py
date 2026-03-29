from dataclasses import dataclass
import datetime
from django.db import models

from appgeneral.models import TimeStampedModel

# Create your models here.

"""
class Sorteo(TimeStampedModel):
    fecha = models.DateField()
    valor_papeleta = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    def __str__(self):
        return f"Sorteo del {self.fecha}"
"""


class Sorteo(models.Model):
    idsorteo = models.AutoField(primary_key=True)
    fecha = models.DateField()
    precio_papeleta = models.DecimalField(max_digits=4, decimal_places=2)
    creado_el = models.DateTimeField()
    modificado_el = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "sorteo"


"""
@dataclass
class SorteoCreadoDto:
    fecha: datetime
    valor_papeleta: float


@dataclass
class SorteoModificadoDto:
    idsorteo: int
    fecha: datetime
    precio_papeleta: float


# mapper
def Sorteo_SorteoDto(sorteo: Sorteo) -> SorteoModificadoDto:
    return SorteoModificadoDto(
        idsorteo=sorteo.idsorteo,
        fecha=sorteo.fecha,
        precio_papeleta=sorteo.precio_papeleta,
    )
"""
