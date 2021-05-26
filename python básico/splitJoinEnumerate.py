# split - dividir uma string
# join - juntar uma lista
# enumerate - enumerar elementos de uma lista


# SPLIT
string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

lista = string.split(' ')
lista2 = string.split(',')

palavra = ''
contagem = 0

for n in lista:
    qtd_vezes = lista.count(n)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = n
print(f'a palavra que apareceu mais foi {palavra}, que apareceu {contagem}x')



# JOIN
nome = 'claudio vitor dantas da silva inacio'
nome_lista = nome.split(' ')
novo_nome = ','.join(nome_lista)
print(novo_nome)



# ENUMERATE
for key, value in enumerate(nome_lista):
    print(f'{key} -> {value}')
