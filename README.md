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

## Estrutura do projeto (resumo)
```
clinica-pet/
├── clinica/           # Projeto Django (settings, urls, wsgi, asgi)
│   └── base/          # App base: views, urls, tests
├── manage.py          # Utilitário de linha de comando do Django
├── pyproject.toml     # Configuração de dependências e Pytest
├── poetry.lock        # Versões travadas das dependências
├── README.md          # Este arquivo
└── .github/workflows/ # Pipeline CI (pytest + cobertura)
```

## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.