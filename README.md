# 🐦 Mini Twitter API - Django REST Framework

Este projeto é uma API backend para uma aplicação estilo Twitter, construída com Django e Django REST Framework. A API permite autenticação de usuários, criação de postagens, funcionalidades de seguir e deixar de seguir usuários, além de um feed personalizado.

---

## 🔧 Tecnologias Utilizadas

- Python 3.11+
- Django 5.2
- Django REST Framework
- PostgreSQL (ou SQLite para dev)
- JWT Authentication
- django-cors-headers
- coverage.py
- drf-yasg (para documentação Swagger)

---

## 🚀 Como Configurar e Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/marcojrdev/PMT-PROJET--MINI-TWITTER-.git
cd PMT-PROJET--MINI-TWITTER-
```

### 2. Crie um ambiente virtual e ative

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

No arquivo `project/settings.py`, configure as credenciais do banco de dados:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sua_db',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Rode o servidor local

```bash
python manage.py runserver
```

Acesse em [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 7. Documentação da API

A documentação Swagger está disponível em: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

---

## 📂 Estrutura do Projeto

```plaintext
manage.py
README.md
requirements.txt
follows/
    __init__.py
    admin.py
    apps.py
    models.py
    serializers.py
    tests.py
    urls.py
    views.py
    migrations/
posts/
    __init__.py
    admin.py
    apps.py
    models.py
    serializers.py
    tests.py
    urls.py
    views.py
    migrations/
project/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
users/
    __init__.py
    admin.py
    apps.py
    models.py
    serializers.py
    tests.py
    urls.py
    views.py
    migrations/
```

---

## 🛠️ Funcionalidades

- **Autenticação de Usuários**: Registro, login e autenticação via JWT.
- **Postagens**: Criação, listagem e curtidas em postagens.
- **Seguir/Deixar de Seguir Usuários**: Gerenciamento de seguidores e seguidos.
- **Feed Personalizado**: Exibição de postagens de usuários seguidos.
- **Documentação Swagger**: Interface interativa para explorar a API.

---

