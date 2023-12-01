import sqlite3

conn = sqlite3.connect('loja')
cursor = conn.cursor()



def cadastrar_cliente(cpf, nome, cep, cidade, estado, numero):
    cursor.execute("INSERT INTO cliente (cpf, nome, cep, cidade, estado, numero) VALUES (?, ?, ?, ?, ?, ?)", (cpf, nome, cep, cidade, estado, numero))
    conn.commit()

def cadastrar_produto(codigo_de_barra, nome_produto, fabricante_produto):
    cursor.execute("INSERT INTO produtos (codigo_de_barra, nome_produto, fabricante_produto) VALUES (?, ?, ?)", (codigo_de_barra, nome_produto, fabricante_produto))
    conn.commit()

def cadastrar_venda(data_venda, hora_venda, cpf_cliente, codigo_de_barra, quantidade, valor_unitario, valor_total):
    cursor.execute("INSERT INTO vendas (data_venda, hora_venda, cpf_cliente, codigo_de_barra, quantidade, valor_unitario, valor_total) VALUES (?, ?, ?, ?, ?, ?, ?)", (data_venda, hora_venda, cpf_cliente, codigo_de_barra, quantidade, valor_unitario, valor_total))
    conn.commit()

def alterar_cliente(cpf, novo_nome, novo_cep, nova_cidade,novo_estado, novo_numero):
    cursor.execute("UPDATE clientes SET nome = ?, cep = ?, cidade = ?, estado = ?, numero = ? WHERE cpf = ?",
                   (novo_nome, novo_cep, nova_cidade, novo_estado, novo_numero, cpf))
    conn.commit()

def alterar_produto(codigo_de_barra, novo_nome, novo_fabricante):
    cursor.execute("UPDATE produtos SET nome_produto = ?, fabricante_produto = ? WHERE codigo_de_barra = ?",
                   (novo_nome, novo_fabricante, codigo_de_barra))
    conn.commit()

def excluir_cliente(cpf):
    cursor.execute('DELETE FROM clientes WHERE cpf = ?', (cpf,))
    conn.commit()

def excluir_produto(codigo_de_barra):
    cursor.execute('DELETE FROM produtos WHERE codigo_de_barra = ?',(codigo_de_barra,))
    conn.commit()

def excluir_venda(data_venda, cpf_cliente):
    cursor.execute('DELETE FROM vendas WHERE data_venda = ? AND cpf_cliente = ?', (data_venda, cpf_cliente))
    conn.commit()

def listar_vendas_por_cpf(cpf):
    cursor.execute('SELECT * FROM vendas WHERE cpf_cliente = ?', (cpf,))
    vendas = cursor.fetchall()
    for venda in vendas:
        print(venda)

def listar_compras_por_codigo_de_barras(codigo_de_barra):
    cursor.execute('SELECT * FROM vendas WHERE codigo_de_barra = ?', (codigo_de_barra,))
    compras = cursor.fetchall()
    for compra in compras:
        print(compra)

def ranking_vendas_por_produto():
    cursor.execute(
        "SELECT codigo_de_barra, SUM(quantidade) as total_vendido FROM vendas GROUP BY codigo_de_barra ORDER BY total_vendido DESC")
    ranking = cursor.fetchall()
    for rank in ranking:
        print(rank)

def ranking_vendas_por_cliente():
    cursor.execute('SELECT cpf_cliente, SUM(valor_total) as total_gasto FROM vendas GROUP BY cpf_cliente ORDER BY total_gasto DESC')
    ranking = cursor.fetchall()
    for rank in ranking:
        print(rank)

#CADASTRO DOS CLIENTES
cadastrar_cliente('22223333444', 'Maria Silva', '89012-485', 'Blumenau', 'SC', '231')
cadastrar_produto('1234567890123', 'Camiseta', 'Adidas')
cadastrar_venda('2023-10-25', '15:00:00', '22223333444', '1234567890123', 5, 49.99, 249.95)
alterar_cliente('12343333555', 'João Pereira', '89012-000', 'Blumenau', 'SC', '156')
alterar_produto('4321567890432', 'Camiseta Esportiva', 'Nike')
excluir_cliente('11199097918')
excluir_produto('7890123456789')
excluir_venda('2023-10-24', '11199097918')
listar_vendas_por_cpf('22223333444')
listar_compras_por_codigo_de_barras('1234567890123')
ranking_vendas_por_produto()
ranking_vendas_por_cliente()

#fechar conexão
conn.close()