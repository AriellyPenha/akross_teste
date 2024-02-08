from django.core.management.base import BaseCommand
from empresa.models import Empresa, Colaborador, Squad
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados fictícios'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')
        empresas = []
        colaboradores = []

        for _ in range(10):
            empresas.append(Empresa.objects.create(nome=fake.company()))

        for _ in range(10):
            cpf = fake.unique.ssn()
            colaboradores.append(Colaborador.objects.create(
                cpf=cpf, 
                data_nascimento=fake.date_of_birth(),
                nome=fake.name()
            ))

        for _ in range(10):
            nome_squad = fake.job()
            empresa = random.choice(empresas)
            squad = Squad.objects.create(nome=nome_squad, empresa=empresa)
            squad.colaboradores.set(random.sample(colaboradores, random.randint(1, 5)))
