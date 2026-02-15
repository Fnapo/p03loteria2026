from django.urls import path

from . import views


urlpatterns = [
    path("", views.listado_sorteos, name="listado_sorteos"),
]
