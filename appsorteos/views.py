from django.shortcuts import render

from .models import Sorteo

# Create your views here.


def listado_sorteos(request):
    sorteos = Sorteo.objects.all()
    return render(request, "listar_sorteos.html", {"sorteos": sorteos})
