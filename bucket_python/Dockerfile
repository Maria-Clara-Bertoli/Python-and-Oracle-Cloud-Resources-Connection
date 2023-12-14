# Use a imagem base do Python
FROM python:3.8-slim

# Crie e defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o código Python para o contêiner
ADD . /app

# Instale as dependências do Oracle Cloud SDK
RUN pip install oci

# Comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "index.py"]
