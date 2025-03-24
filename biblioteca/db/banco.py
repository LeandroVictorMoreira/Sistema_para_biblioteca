import mysql.connector

meudb = mysql.connector.connect (
    host ='localhost',
    user  = 'root',
    password ='pass09',
    database = 'biblioteca_system'
) #Chamada do banco de dados

cursor = meudb.cursor()

cursor.execute ("Select * from leitores")

on_db = cursor.fetchall()

print(on_db)