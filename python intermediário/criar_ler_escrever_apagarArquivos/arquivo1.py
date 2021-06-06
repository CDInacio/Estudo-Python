# 'r' -> abre para leitura (padrão)
# 'w' -> abre para escrita, truncando o arquivo primeiro (removendo tudo o que estiver contido no mesmo)
# 'w' -> abre para criação exclusiva, falhando caso o arquivo exista
# 'a' -> abre para escrita, anexando ao final do arquivo caso o mesmo exista
# 'b' -> binary mode
# 't' -> modo texto (padrão)
# '+' -> aberto para atualização (leitura e escrita)


file = open('abc.txt', 'w+')     # leitura e escrita
file.write('linha1\n')
file.write('linha2\n')
file.write('linha3\n')

file.seek(0, 0)    # chamando o cursor pra posição inicial do arquivo
print('lendo linhas:')
print(file.read())
print('-' * 50)

file.seek(0, 0)     # voltando o cursor pra posição inicial do arquivo
# lendo linha por linha
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')
print('-' * 50)

file.seek(0, 0)    # chamando o cursor pra posição inicial do arquivo

# print(file.readlines()) == for value in file:
for value in file:  # == for value in file.readlines():
    print(value, end='')

file.close()