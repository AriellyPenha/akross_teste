from django.db import models
from django.utils.translation import gettext as _


class Empresa(models.Model):
    nome = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Nome da Empresa"
    )

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

    def __str__(self):
        return self.nome


class Colaborador(models.Model):
    cpf = models.CharField(max_length=14, null=False, blank=False, unique=True)
    data_nascimento = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True
    )
    nome = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Nome do colaborador"
    )

    class Meta:
        verbose_name = _("Colaborador")
        verbose_name_plural = _("Colaboradores")

    def __str__(self):
        return self.nome


class Squad(models.Model):
    nome = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Nome do Squad"
    )
    colaboradores = models.ManyToManyField(
        Colaborador, verbose_name=_("Empregados"), related_name="squads"
    )
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        verbose_name=_("Empresa"),
    )

    class Meta:
        verbose_name = _("Squad")
        verbose_name_plural = _("Squads")

    def __str__(self):
        return self.nome
