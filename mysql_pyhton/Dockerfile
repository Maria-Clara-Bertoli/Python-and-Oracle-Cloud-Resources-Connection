# Use a imagem oficial do Python como base
FROM python:3.9

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt e index.py para o contêiner
COPY requirements.txt .
COPY index.py .

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para executar o script Python
CMD ["python", "index.py"]
