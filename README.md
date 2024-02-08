# Instalando Projeto

## Inicializando VM
```Entrar na pasta akross_vm/Scripts > Executar o comando ".\activate" ```

``` Após iniciarlizar a vm, entrar na pasta akross > Executar o comando "pip install -r requirements.txt" para instalar os pacotes necessários. ```

## Executando as migrações
``` Rodar as migrações > "python manage.py migrate" ```

## Inserindo dados fakes
``` Popular o banco > "python manage.py popular_db" ```

## Criando usuário para cadastrar novos dados
``` Para inserir os dados manualmente, primeiro precisará de um usuário > "python manage.py createsuperuser" ```

``` Após criar o usuário, suba a aplicação e acesse o 'http://localhost:8000/admin' e realize o login com o super usuário```

## Rotas

    - admin/
    - empresa/ [name='lista_empresas']
    - empresa/<int:empresa_id>/squads/ [name='lista_squads']
    - squads/<int:squad_id>/colaboradores/ [name='lista_colaboradores']
    - colaboradores/<int:colaborador_id> [name='detalhe_colaborador']



## Referencias

- https://docs.djangoproject.com/en/5.0/intro/
- https://getbootstrap.com/docs/4.1/content/tables/
- https://datatables.net/
