from datetime import datetime, timedelta
from django.shortcuts import redirect, render

from .models import Sorteo

# Create your views here.


def listado_sorteos(request):
    sorteos = Sorteo.objects.all()

    return render(request, "listar_sorteos.html", {"sorteos": sorteos})


def crear_sorteo(request):
    # Aquí iría la lógica para crear un nuevo sorteo
    if request.method == "POST":
        # Procesar el formulario y crear el sorteo
        fecha = request.POST.get("fecha")
        valor_papeleta = request.POST.get("valor_papeleta")
        Sorteo.objects.create(fecha=fecha, valor_papeleta=valor_papeleta)

        return redirect("listar_sorteos")

    fecha_minima = datetime.now() + timedelta(days=7)
    fecha_maxima = datetime.now() + timedelta(days=120)

    return render(
        request,
        "crear_sorteo.html",
        {"fecha_minima": fecha_minima.date(), "fecha_maxima": fecha_maxima.date()},
    )


def detalles_sorteo(request, sorteo_id):
    try:
        sorteo = Sorteo.objects.get(id=sorteo_id)
    except Sorteo.DoesNotExist:
        # Manejar el caso en que no exista el sorteo
        return render(request, "error_sorteo.html", {"mensaje": "El Sorteo no existe."})

    return render(request, "detalles_sorteo.html", {"sorteo": sorteo})
