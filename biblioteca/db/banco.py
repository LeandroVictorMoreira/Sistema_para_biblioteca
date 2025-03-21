import _mysql_connector

meudb = _mysql_connector.connect (
    host ='localhost',
    user  = 'root',
    passoword ='pass09',
    database = 'biblioteca_system'
) #Chamada do banco de dados