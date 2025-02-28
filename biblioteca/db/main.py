import mysql.connector #Fazer a importação do conector do MySql

meudb = mysql.connector.connect(  #conexão ao servidor
host = 'localhost',
user = 'root',
password = 'pass09',
database =  'sistema_para_biblioteca'

)


#Criar novo banco de dados


cursor = meudb.cursor() #Definição do cursor
cursor.execute("SHOW DATABASES LIKE'biblioteca_dados'") 


resultado = cursor.fetchall()

if resultado: #Função para verificar a existência do Banco de Dados
    print("O banco de dados já existe.")
else:
    print("O banco de dados ainda não existe.")
    cursor.execute("CREATE DATABASE biblioteca_dados")


# Criação de uma nova tabela

cursor.execute("CREATE TABLE leitores(Id INT AUTO_INCREMENT PRIMARY KEY), nome (VARCHAR(255))") 

sql = "INSERT INTO clientes (nome) VALUE(%s)"
values = ("João Pedro,")


cursos.execute()