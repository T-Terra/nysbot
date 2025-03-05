# Usar uma imagem oficial do Python 3.12
FROM python:3.12

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto para dentro do container
COPY . /app

# Instalar Poetry
RUN pip install poetry

# Instalar dependências do projeto
RUN poetry install --no-root

RUN echo "Username: $DJANGO_SUPERUSER_USERNAME" && \
    poetry run python manage.py migrate && \
    poetry run python manage.py shell -c 'from django.contrib.auth import get_user_model; \
    User = get_user_model(); \
    User.objects.create_superuser("$DJANGO_SUPERUSER_USERNAME", "", "$DJANGO_SUPERUSER_PASSWORD")' || true

# Comando para rodar o app (mude conforme necessário)
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]