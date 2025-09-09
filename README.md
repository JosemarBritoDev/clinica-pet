# Clinica Pet

Sistema para gestão de clínicas veterinárias (Django).

Este repositório está preparado para desenvolvimento local com Poetry, testes com Pytest e integração contínua via GitHub Actions.

## Sumário
- Visão geral
- Requisitos
- Instalação e configuração (passo a passo)
- Executando a aplicação
- Executando testes e cobertura
- Comandos úteis com Poetry
- Estrutura do projeto
- Licença

## Requisitos
- Python 3.13+
- Poetry (gerenciador de dependências)

## Instalação e configuração
Após clonar o repositório:

1. Instale as dependências (incluindo as de desenvolvimento):
   ```bash
   poetry install --with dev
   ```

2. (Opcional) Ative o ambiente virtual gerenciado pelo Poetry:
   ```bash
   poetry shell
   ```
   Você também pode executar qualquer comando prefixando com `poetry run` sem ativar o shell.

3. Aplique as migrações do banco de dados:
   ```bash
   poetry run python manage.py migrate
   ```

4. (Opcional) Crie um superusuário para acessar o admin:
   ```bash
   poetry run python manage.py createsuperuser
   ```

## Executando a aplicação
Inicie o servidor de desenvolvimento:
```bash
poetry run python manage.py runserver
```
A aplicação padrão ficará disponível em http://127.0.0.1:8000/.

## Executando testes e cobertura
- Rodar a suíte de testes:
  ```bash
  poetry run pytest -q
  ```

- Rodar testes com cobertura de código do pacote `clinica` e gerar relatório HTML em `htmlcov/`:
  ```bash
  poetry run pytest -q --cov=clinica --cov-report=html
  ```

> Observação: o projeto já define `DJANGO_SETTINGS_MODULE=clinica.settings` em `pyproject.toml` para o Pytest.

## Comandos úteis com Poetry
- Atualizar o Poetry e instalar dependências do projeto:
  ```bash
  python -m pip install --upgrade pip
  python -m pip install poetry
  poetry install --with dev
  ```
- Regenerar o arquivo de lock (sem atualizar versões):
  ```bash
  poetry lock --no-update
  ```
- Executar um comando no ambiente virtual sem ativar o shell:
  ```bash
  poetry run <comando>
  ```

## Estrutura do projeto (atualizada)
```
clinica-pet/
├── clinica/                        # Projeto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                 # Configurações do Django
│   ├── urls.py                     # Rotas do projeto
│   ├── wsgi.py
│   └── base/                       # App base (clientes)
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── migrations/
│       ├── models.py
│       ├── services/               # Regras de negócio
│       │   ├── cliente_service.py
│       │   └── endereco_service.py
│       ├── entidades/              # Objetos de domínio
│       │   ├── cliente.py
│       │   └── endereco.py
│       ├── forms/
│       │   ├── cliente_forms.py
│       │   └── endereco_forms.py
│       ├── templates/
│       │   ├── base.html
│       │   └── clientes/
│       │       └── form_cliente.html
│       ├── templatetags/
│       │   └── meus_filtros.py
│       ├── urls.py                 # Rotas do app
│       ├── views/
│       │   └── cliente_views.py
│       └── tests.py
├── manage.py                       # Utilitário de linha de comando do Django
├── conftest.py                     # Configuração do Pytest
├── pyproject.toml                  # Dependências e configurações (inclui Pytest)
├── poetry.lock                     # Versões travadas das dependências
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        └── git-action.yml          # Pipeline CI (pytest + cobertura)
```
> Observações:
> - A pasta htmlcov/ é gerada apenas quando a cobertura é executada e normalmente é ignorada pelo Git.
> - O banco de dados local (db.sqlite3) é gerado em desenvolvimento e não é necessário em produção.

## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.