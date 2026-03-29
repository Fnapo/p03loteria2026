from django.db import models

# Create your models here.


class Socio(models.Model):
    idsocio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    municipio = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100)
    movil = models.CharField(max_length=15)
    provincia = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = "socio"
