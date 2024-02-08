from django.shortcuts import render, get_object_or_404

from django.views.generic import View

from .models import Empresa, Squad, Colaborador


class EmpresaListView(View):
    def get(self, request):
        empresas = Empresa.objects.all()
        context = {"empresas": empresas}
        return render(request, "empresa/lista_empresas.html", context=context)


class SquadListView(View):
    def get(self, request, empresa_id):
        squads = Squad.objects.filter(empresa_id=empresa_id)
        empresa = Empresa.objects.get(id=empresa_id)
        context = {"squads": squads, "empresa": empresa}
        return render(request, "squads/lista_squads.html", context=context)


class ColaboradorListView(View):
    def get(self, request, squad_id):

        squad = get_object_or_404(Squad, id=squad_id)
        empresa = Empresa.objects.get(id=squad.empresa_id)
        colaboradores = squad.colaboradores.all()
        context = {"empresa": empresa, "squad": squad, "colaboradores": colaboradores}
        return render(request, "colaborador/lista_colaboradores.html", context=context)


class ColaboradorDetailView(View):
    def get(self, request, colaborador_id):
        colaborador = Colaborador.objects.get(id=colaborador_id)
        context = {"colaborador": colaborador}
        return render(request, "colaborador/detalhe_colaborador.html", context=context)
