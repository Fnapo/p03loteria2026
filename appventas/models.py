from django.db import models

from appsocios.models import Socio
from appsorteos.models import Sorteo

# Create your models here.


class SocioSorteo(models.Model):
    pk = models.CompositePrimaryKey("socio_fk", "sorteo_fk")
    socio_fk = models.ForeignKey(Socio, models.CASCADE, db_column="socio_fk")
    sorteo_fk = models.ForeignKey(Sorteo, models.CASCADE, db_column="sorteo_fk")
    pagado = models.DecimalField(max_digits=8, decimal_places=2)
    deuda = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        managed = False
        db_table = "socio_sorteo"
