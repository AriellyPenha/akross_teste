# Exemplo de urlpatterns em seu arquivo urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("empresa/", views.EmpresaListView.as_view(), name="lista_empresas"),
    path(
        "empresa/<int:empresa_id>/squads/",
        views.SquadListView.as_view(),
        name="lista_squads",
    ),
    path(
        "squads/<int:squad_id>/colaboradores/",
        views.ColaboradorListView.as_view(),
        name="lista_colaboradores",
    ),
    path(
        "colaboradores/<int:colaborador_id>",
        views.ColaboradorDetailView.as_view(),
        name="detalhe_colaborador",
    ),
]
