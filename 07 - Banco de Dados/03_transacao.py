import sqlite3

conexao = sqlite3.connect("clientes.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste 1", "teste1@gmail.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?, ?,?)", (2, "Teste 2", "teste2@gmail.com"))
except Exception as exc:
    print(f"Ops! Um erro ocorreu! {exc}")
    conexao.rollback()
