from django.shortcuts import redirect, render

from appsorteos.models import Sorteo
from .models import SocioSorteo

# Create your views here.


def elegir_sorteo_venta(request):
    if request.method == "POST":
        sorteo_id = request.POST.get("sorteo")

        return redirect("deudas_sorteo", sorteo_id=sorteo_id)
    sorteos = Sorteo.objects.all().order_by("-fecha")
    if not sorteos.exists():
        # return redirect("deudas_sorteo", sorteo_id=1)
        return render(
            request,
            "error_sorteo.html",
            {"mensaje": "No hay sorteos disponibles."},
        )

    return render(
        request,
        "elegir_sorteo_venta.html",
        {"sorteos": sorteos},
    )


def deudas_sorteo(request, sorteo_id):
    # Aquí iría la lógica para mostrar las deudas de un sorteo específico.
    deudas = SocioSorteo.objects.filter(sorteo_fk=sorteo_id)
    if not deudas.exists():
        return render(
            request,
            "error_sorteo.html",
            {"mensaje": "No hay deudas para este sorteo."},
        )

    return render(request, "deudas_sorteo.html", {"deudas": deudas})
