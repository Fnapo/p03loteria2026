from datetime import datetime
from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # No table will be created for this model
