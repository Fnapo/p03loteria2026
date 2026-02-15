from django.urls import path

from . import views


urlpatterns = [
    path("", views.listado_sorteos, name="listar_sorteos"),
    path("crear/", views.crear_sorteo, name="crear_sorteo"),
    # path("<int:sorteo_id>/", views.detalles_sorteo, name="detalles_sorteo"),
]
