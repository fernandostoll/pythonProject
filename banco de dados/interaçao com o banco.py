import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='microsoft'
)

cursor = conexao.cursor()
query = ('INSERT INTO softwares'
         '(nome, versao, descricao, requisitos, valor, data_cadastro)VALUES'
         '("Excel", "2021.01", "windows XP SP3", "internet", 150.00, "2021-02-03")')
cursor.execute(query)

#fetch para select, commit para insert, update, delete...
#resultado = cursor.fetchall()

conexao.commit()

#for linha in resultado:
#    print(linha)

cursor.close()
conexao.close()