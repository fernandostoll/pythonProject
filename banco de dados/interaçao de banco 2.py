import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='microsoft'
)
dados = ['power Point 2021', '2021.01', 'novo power point', 'paciencia', 250.00, '2023-10-19']

cursor = conexao.cursor()


query = (f'INSERT INTO softwares'
         f'(nome, versao, descricao, requisitos, valor, data_cadastro)VALUES(%s,%s,%s,%s,%s,%s)')

cursor.execute(query, (dados[0], dados[1], dados[2], dados[3], dados[4], dados[5]))

#fetch para select, commit para insert, update, delete...
#resultado = cursor.fetchall()

conexao.commit()
cursor.close()
conexao.close()