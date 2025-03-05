# Usar uma imagem oficial do Python 3.12
FROM python:3.12

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto
COPY . .

# Instalar Poetry
RUN pip install poetry

# Instalar dependências do projeto
RUN poetry install

# Comando para rodar o app (mude conforme necessário)
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]