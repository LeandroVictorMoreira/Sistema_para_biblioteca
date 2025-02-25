import mysql.connector #Fazer a importação do conector do MySql

meudb = mysql.connector.connect(  #conexão ao servidor
host = 'localhost',
user = 'root',
password = 'pass09',
database =  'sistema_para_biblioteca'

)


#Criar novo banco de dados


cursor = meudb.cursor()
cursor.execute("")