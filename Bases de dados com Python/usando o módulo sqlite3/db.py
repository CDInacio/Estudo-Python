import sqlite3

conexao = sqlite3.connect('baseDeDados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')


cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('maria', 65.8))
conexao.commit()

cursor.execute('SELECT * FROM clientes')

for value in cursor.fetchall():
    identificador, nome, peso = value
    print(identificador, nome, peso)
    
# for value in cursor.fetchall():
#     print(value)

cursor.close()
conexao.close()
