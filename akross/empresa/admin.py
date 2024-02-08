from django.contrib import admin
from .models import Squad, Colaborador, Empresa
from easy_select2 import select2_modelform

# Register your models here.


@admin.register(Squad)
class SquadAdmin(admin.ModelAdmin):
    """Admin View for Squad"""

    form = select2_modelform(Squad)
    list_display = ["id", "nome", "empresa_nome"]
    ordering = ("id",)

    def empresa_nome(self, obj):
        return obj.empresa.nome

    empresa_nome.short_description = "Nome da empresa"


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    """Admin View for Colaborador"""

    form = select2_modelform(Colaborador)
    list_display = ["id", "nome", "cpf"]
    ordering = ("id",)


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    """Admin View for empresa"""

    form = select2_modelform(Empresa)
    list_display = ["id", "nome"]
    ordering = ("id",)
