from django.urls import path

from . import views

urlpatterns = [
    path("elegir_sorteo_venta/", views.elegir_sorteo_venta, name="elegir_sorteo_venta"),
    path("deudas/<int:sorteo_id>/", views.deudas_sorteo, name="deudas_sorteo"),
]
