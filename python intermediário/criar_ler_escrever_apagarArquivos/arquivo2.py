# 'r' -> abre para leitura (padrão)
# 'w' -> abre para escrita, truncando o arquivo primeiro (removendo tudo o que estiver contido no mesmo)
# 'w' -> abre para criação exclusiva, falhando caso o arquivo exista
# 'a' -> abre para escrita, anexando ao final do arquivo caso o mesmo exista
# 'b' -> binary mode
# 't' -> modo texto (padrão)
# '+' -> aberto para atualização (leitura e escrita)

# melhor maneira para a abertura de arquivos

"""""
with open('abc2.txt', 'w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')
    file.write('linha 4\n')

    file.seek(0)
    print(file.read())
"""


with open('abc2.txt', 'a+') as file:
    file.write('adiciona uma linha sem apagar as anteriores\n')

    file.seek(0)
    print(file.read())

