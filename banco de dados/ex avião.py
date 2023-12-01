import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="aeroporto"
)

cursor = db.cursor()

def cadastrar_aeronave(nome, assentos):
    cursor.execute('INSERT INTO Aeronaves (nome, assentos) VALUES (%s, %s)', (nome, assentos))
    db.commit()

def editar_aeronave(aeronave_id, nome, assentos):
    cursor.execute('UPDATE Aeronaves SET Nome = %s, Assentos = %s WHERE ID = %s', (nome, assentos, aeronave_id))
    db.commit()

def excluir_aeronave(aeronave_id):
    cursor.execute('DELETE FROM Aeronaves WHERE ID = %s', (aeronave_id,))
    db.commit()

def gerar_relatorio(periodo, empresa, aeroporto):
    pass

cadastrar_aeronave('Boeing 737', 150,)
cadastrar_aeronave('Airbus A380', 489,)
editar_aeronave(3, 'Boeing 737', 140)
editar_aeronave(1, 'Airbus A320', 180)
gerar_relatorio(3, "Boeing", 'navegantes')
#excluir_aeronave(2)

#para fechar conexão
db.close()


