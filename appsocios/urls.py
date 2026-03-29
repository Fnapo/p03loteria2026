from django.urls import path

from . import views


urlpatterns = [
    path("", views.listado_socios, name="listar_socios"),
    path("inscribir/", views.inscribir_socio, name="inscribir_socio"),
    path("detalles/<int:socio_id>/", views.detalles_socio, name="detalles_socio"),
]
