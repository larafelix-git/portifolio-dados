import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="08101991",
        database="sistema_medico_agendamentos"
    )
