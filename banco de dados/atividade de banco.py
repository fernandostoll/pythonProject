# criar um programa que faça as seguintes funçoes:
# criar banco
# criar tabela do banco
# e permite ao usuario interagir com ele por meio de:
# inserir registros - INSERT
# editar registros (nome, estado civil) - UPDATE
# apagar registros (pelo CPF - consultaar id) - DELETE
# consultar registros (filtrar por data, cidade, estado) - SELECT
# o banco de dados modelado contem apenas 1 tabela, com as seguintes colunas
# id, cpf, nome, estado civil, CEP + (cidade, estado, bairro e rua)
# informaçoes do CEP devem ser coletados atraves de requests no VIACEP

import mysql.connector
import requests

def criar_banco():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS meu_banco")
    conn.close()

def criar_tabela():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="meu_banco"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS registros (id INT AUTO_INCREMENT PRIMARY KEY, cpf VARCHAR(11), nome VARCHAR(255), estado_civil VARCHAR(50), cidade VARCHAR(255), estado VARCHAR(50), bairro VARCHAR(255), rua VARCHAR(255))")
    conn.close()

def inserir_registro(cpf, nome, estado_civil, cep):
    cep_info = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
    cidade = cep_info.get('localidade')
    estado = cep_info.get('uf')
    bairro = cep_info.get('bairro')
    rua = cep_info.get('logradouro')

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="meu_banco"
    )

    cursor = conn.cursor()
    cursor.execute("INSERT INTO registros (cpf, nome, estado_civil, cidade, estado, bairro, rua) VALUES (%s, %s, %s, %s, %s, %s, %s)", (cpf, nome, estado_civil, cidade, estado, bairro, rua))
    conn.commit()
    conn.close()

def atualizar_registro(cpf, novo_nome, novo_estado_civil):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="meu_banco"
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE registros SET nome = %s, estado_civil = %s WHERE cpf = %s", (novo_nome, novo_estado_civil, cpf))
    conn.commit()
    conn.close()

def apagar_registro(cpf):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="meu_banco"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM registros WHERE cpf = %s", (cpf,))
    conn.commit()
    conn.close()

def consultar_registro(filtro):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="meu_banco",
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registros WHERE cidade = %s OR estado = %s OR data = %s", (filtro, filtro, filtro))
    resultados = cursor.fetchall()
    conn.close()
    return resultados


inserir_registro("11199097918", "Fernando", "Solteiro", "89050000")

#atualizar_registro("12345678901", "João", "Casado")

#nserir_registro("11194009732", "Maria", "Solteiro", "89010500")


#apagar_registro("12345678901")

#consulta de registros
resultados = consultar_registro("São paulo")
for resultado in resultados:
    print(resultado)