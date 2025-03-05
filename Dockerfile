# Usar uma imagem oficial do Python 3.12
FROM python:3.12

# Criar diretório de trabalho
WORKDIR /

# Copiar arquivos do projeto para dentro do container
COPY . /

# Instalar Poetry
RUN pip install poetry

# Instalar dependências do projeto
RUN poetry install --no-root

RUN mkdir -p /staticfiles

RUN poetry run python manage.py migrate && \
    poetry run python manage.py collectstatic --noinput && \
    poetry run python create_superuser.py || true

# Comando para rodar o app (mude conforme necessário)
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]