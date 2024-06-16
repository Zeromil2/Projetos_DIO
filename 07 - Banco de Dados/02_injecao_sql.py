import sqlite3

conexao = sqlite3.connect("clientes.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe o id do cliente: ")  # responder: 1 OR 1=1
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}") 

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))
