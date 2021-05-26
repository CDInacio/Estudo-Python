lista = [
    ('chave1', 'valor'),
    ('chave2', 'valor2')
]

dicionario = {key: value for key, value in lista}
print(dicionario)

# gerando um dicionario
dicionario2 = {key:value for key, value in enumerate(range(10))}
print(dicionario2)

# outra forma de criar um dicionario
dicionario3 = {f'chave{value}': value ** 2 for value in range(5)}
print(dicionario3)