import mysql.connector

# Configurações de Conexão
host = 'localhost'
usuario = 'admin'
senha = 'xxxxxxxx'

# Conectar ao Servidor MySQL
conexao_servidor = mysql.connector.connect(
    host=host,
    user=usuario,
    password=senha
)

# Cria um cursor para executar consultas SQL
cursor_servidor = conexao_servidor.cursor()

# Criar Banco de Dados
cursor_servidor.execute("CREATE DATABASE IF NOT EXISTS banco_pessoa")
conexao_servidor.commit()

# Conectar ao Banco de Dados Criado
conexao = mysql.connector.connect(
    host=host,
    user=usuario,
    password=senha,
    database='banco_pessoa'
)

# Cria um cursor para executar consultas SQL no novo banco de dados
cursor = conexao.cursor()

# Criar Tabela "pessoa"
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoa (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        contato VARCHAR(255) NOT NULL
    )
""")
conexao.commit()

# Inserir Dados na Tabela
cursor.execute("INSERT INTO pessoa (nome, contato) VALUES (%s, %s)", ("Ana", "123456789"))
cursor.execute("INSERT INTO pessoa (nome, contato) VALUES (%s, %s)", ("Bruno", "987654321"))
conexao.commit()

# Listar Dados da Tabela
cursor.execute("SELECT * FROM pessoa")
resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

# Fechar Cursores e Conexões
cursor.close()
cursor_servidor.close()
conexao.close()
conexao_servidor.close()


