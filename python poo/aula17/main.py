"""""
class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()


with Arquivo('arquivo.txt', 'w') as file:
    file.write('alguma coisa')
"""""

# outra forma de criar um gerenciador de contexto( sem usar classes)

from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print('abrindo arquivo!')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('fechando arquivo!')
        arquivo.close()


with abrir('arquivo2.txt', 'w') as file:
    file.write('ola mundo')
