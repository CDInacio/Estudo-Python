import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


# inserindo um registro por vez
# with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'INSERT INTO clientes(nome, sobrenome, idade, peso) VALUES (%s, #%s, %s, %s)'
#        cursor.execute(sql, ('Cláudio', 'Dantas', 24, 100))
#        conexao.commit()


# inserindo mais de um registro por vez
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes(nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'

        dados = [
            ('Natália', 'Paiva', 24, 60),
            ('Cláudio', 'Inácio', 60, 120),
            ('Sandro', 'Dantas', 24, 60),
        ]

        # cursor.executemany(sql, dados)
        # conexao.commit()


#  apagando um registro
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         # cursor.execute(sql, (5,))
#         # conexao.commit()


# apagando mais de um registro de uma vez
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
        # cursor.execute(sql, (5, 6, 7))
        # conexao.commit()


# gerenciador de contexto da conexao
with conecta() as conexao:
    # gerenciador de contexto do cursor
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY nome ASC LIMIT 20')
        resultado = cursor.fetchall()

        for row in resultado:
            # print(row['nome'], row['sobrenome'])
            print(row)
