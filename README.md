# Clínica Pet

Sistema para gestão de clínicas veterinárias desenvolvido com Django. Este repositório está preparado para desenvolvimento local com Poetry, testes com Pytest e relatório de cobertura.

## Sumário
- Visão geral
- Requisitos
- Instalação e configuração
- Banco de dados (MySQL)
- Executando a aplicação
- Testes e cobertura
- Qualidade de código
- Comandos úteis (Poetry)
- Estrutura do projeto (completa)
- Licença

## Visão geral
Aplicação web para cadastro e gerenciamento de clientes de uma clínica veterinária. Inclui camadas de entidades, serviços, formulários, views e templates, além de filtros de template customizados.

## Requisitos
- Python 3.10–3.12 (recomendado 3.11 no WSL)
- Poetry (gerenciador de dependências)
- MySQL Server 8+ (para execução com as configurações padrão do projeto)

## Instalação e configuração
1) Instale as dependências do projeto (incluindo as de desenvolvimento):
```bash
python -m pip install --upgrade pip
python -m pip install poetry
poetry install --with dev
```

2) (Opcional) Ative o ambiente virtual do Poetry:
```bash
poetry shell
```
Você também pode usar `poetry run <comando>` sem ativar o shell.

### Ambiente no WSL (Ubuntu)
Se você estiver usando WSL (ex.: Ubuntu 22.04):
1. Instale Python 3.11 (recomendado) e ferramentas:
   ```bash
   sudo apt update
   sudo apt install -y python3.11 python3.11-venv python3.11-distutils build-essential python3-pip
   ```
2. Instale o Poetry no WSL e configure o ambiente virtual dentro do projeto (já há um arquivo `poetry.toml` com `in-project = true`):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   exec "$HOME/.local/bin/poetry" --version
   poetry env use python3.11
   poetry install --with dev
   ```
3. Se precisar do MySQL no WSL para rodar a aplicação com o banco padrão, instale dependências nativas para compilar `mysqlclient`:
   ```bash
   sudo apt install -y default-libmysqlclient-dev pkg-config
   ```
   Caso não use MySQL durante o desenvolvimento, você pode ajustar temporariamente o `DATABASES` no `clinica/settings.py` para SQLite.
4. No seu IDE (PyCharm/IntelliJ/VS Code), selecione o interpretador do WSL apontando para `.venv/bin/python` dentro do projeto no WSL.

## Banco de dados (MySQL)
O projeto está configurado para usar MySQL por padrão em `clinica/settings.py`:
- HOST: 127.0.0.1
- PORT: 3306
- NAME: clinica_pet_db
- USER: root
- PASSWORD: clinica1305

Passos recomendados para ambiente local:
- Instale e inicie o MySQL Server 8+.
- Crie o banco de dados:
  ```sql
  CREATE DATABASE clinica_pet_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  ```
- Ajuste usuário e senha conforme seu ambiente (se necessário) e atualize `clinica/settings.py`.
- Certifique-se de ter as bibliotecas de desenvolvimento do MySQL instaladas para compilar/instalar `mysqlclient` (no Linux: libmysqlclient-dev; no macOS: `brew install mysql-client`; no Windows recomenda-se usar WSL).

Aplicando migrações e criando superusuário:
```bash
poetry run python manage.py migrate
poetry run python manage.py createsuperuser  # opcional, para acessar /admin
```

Observação: Existe um arquivo `db.sqlite3` no repositório para fins de desenvolvimento/testes, mas as configurações atuais apontam para MySQL. Se preferir SQLite para um “quick start”, altere temporariamente o bloco DATABASES em `clinica/settings.py` para usar sqlite3.

## Executando a aplicação
Inicie o servidor de desenvolvimento:
```bash
poetry run python manage.py runserver
```
Acesse: http://127.0.0.1:8000/

## Testes e cobertura
- Executar a suíte de testes:
```bash
poetry run pytest -q
```

- Executar testes com cobertura (gera relatório HTML em `htmlcov/`):
```bash
poetry run pytest -q --cov=clinica --cov-report=html
```

Dica: O arquivo `pytest.ini` define `DJANGO_SETTINGS_MODULE=clinica.settings` e os padrões de descoberta de testes.

## Qualidade de código
- Rodar Flake8:
```bash
poetry run flake8
```

## Comandos úteis (Poetry)
- Atualizar o lock sem atualizar versões:
```bash
poetry lock --no-update
```
- Executar um comando no ambiente virtual sem ativar o shell:
```bash
poetry run <comando>
```

## Estrutura do projeto (completa)
Abaixo está a árvore completa com todas as pastas e arquivos presentes neste repositório:

```
clinica-pet
├─ LICENSE
├─ README.md
├─ anotacoes.txt
├─ clinica
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ base
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ entidades
│  │  │  ├─ cliente.py
│  │  │  └─ endereco.py
│  │  ├─ forms
│  │  │  ├─ cliente_forms.py
│  │  │  └─ endereco_forms.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_alter_cliente_cpf_alter_enderecocliente_cep_and_more.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ services
│  │  │  ├─ cliente_service.py
│  │  │  └─ endereco_service.py
│  │  ├─ templates
│  │  │  ├─ base.html
│  │  │  └─ clientes
│  │  │     ├─ confirma_exclusao.html
│  │  │     ├─ form_cliente.html
│  │  │     ├─ lista_cliente.html
│  │  │     └─ lista_clientes.html
│  │  ├─ templatetags
│  │  │  └─ meus_filtros.py
│  │  ├─ tests
│  │  │  ├─ __init__.py
│  │  │  ├─ test_cliente_service.py
│  │  │  ├─ test_cliente_views.py
│  │  │  ├─ test_entidades.py
│  │  │  ├─ test_home_views.py
│  │  │  ├─ test_meus_filtros.py
│  │  │  └─ tests_models.py
│  │  ├─ urls.py
│  │  └─ views
│  │     └─ cliente_views.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ conftest.py
├─ db.sqlite3
├─ htmlcov
│  ├─ class_index.html
│  ├─ coverage_html_cb_6fb7b396.js
│  ├─ favicon_32_cb_58284776.png
│  ├─ function_index.html
│  ├─ index.html
│  ├─ keybd_closed_cb_ce680311.png
│  ├─ status.json
│  ├─ style_cb_6b508a39.css
│  ├─ z_93fa48e1be93dc68___init___py.html
│  ├─ z_93fa48e1be93dc68_asgi_py.html
│  ├─ z_93fa48e1be93dc68_settings_py.html
│  ├─ z_93fa48e1be93dc68_urls_py.html
│  ├─ z_93fa48e1be93dc68_wsgi_py.html
│  ├─ z_989e13946f0551f7___init___py.html
│  ├─ z_989e13946f0551f7_admin_py.html
│  ├─ z_989e13946f0551f7_apps_py.html
│  ├─ z_989e13946f0551f7_models_py.html
│  ├─ z_989e13946f0551f7_tests_py.html
│  ├─ z_989e13946f0551f7_urls_py.html
│  ├─ z_989e13946f0551f7_views_py.html
│  ├─ z_c1bf7dc1ede8e3bd___init___py.html
├─ manage.py
├─ poetry.lock
└─ pyproject.toml
```

Notas:
- A pasta `htmlcov/` e o arquivo `db.sqlite3` são artefatos locais de desenvolvimento.
- Ajuste as credenciais de banco no `settings.py` para seu ambiente.

## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.