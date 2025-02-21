import mysql.connector

meudb = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = 'pass09',
database =  'sistema_para_biblioteca'

)

cursor = meudb.cursor()