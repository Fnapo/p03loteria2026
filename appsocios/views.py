from django.shortcuts import redirect, render

from .models import Socio

# Create your views here.


def listado_socios(request):
    socios = Socio.objects.all()

    return render(request, "listar_socios.html", {"socios": socios})


def inscribir_socio(request):
    # Aquí iría la lógica para inscribir un nuevo socio
    if request.method == "POST":
        # Procesar el formulario y crear el sorteo
        fecha = request.POST.get("fecha")
        valor_papeleta = request.POST.get("valor_papeleta")
        Socio.objects.create(fecha=fecha, valor_papeleta=valor_papeleta)

        return redirect("listar_socios")

    return render(
        request,
        "inscribir_socio.html",
    )
    pass


def detalles_socio(request, socio_id):
    # Aquí iría la lógica para mostrar los detalles de un socio específico
    pass
