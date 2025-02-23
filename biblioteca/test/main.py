import mysql.connector #Fazer a importação do conector do MySql

meudb = mysql.connector.connect( 
host = 'localhost',
user = 'root',
password = 'pass09',
database =  'sistema_para_biblioteca'

)# Uma varivavel que chama o MySql

cursor = meudb.cursor()

cursor.execute("SELECT * FROM alunos") #Selector de Tabela

meuresultado =cursor.fetchall()


print(meuresultado)