# List Comprehension é uma forma concisa de criar e manipular listas.
produtos = [
    {'nome': 'produto1', 'preco': 10},
    {'nome': 'produto2', 'preco': 20.90},
    {'nome': 'produto3', 'preco': 40},
    {'nome': 'produto4', 'preco': 50.99},
    {'nome': 'produto5', 'preco': 70.50},
    {'nome': 'produto6', 'preco': 10},
    {'nome': 'produto7', 'preco': 5.99},
    {'nome': 'produto8', 'preco': 57}
]

lista1 = [1, 2, 3, 4, 5]
lista2 = ['claudio', 'vitor', 'dantas']

# jogando cada valor iterado no primeiro value e criando uma lista
exp2 = [value for value in lista1]
print(exp2)

# multiplicando cada elemento da lista 1 por 2 e criando uma nova lista(exp3)
exp3 = [value * 2 for value in lista1]
print(exp3)

#criando uma tupla
exp4 = [(value, value2) for value in lista1 for value2 in range(3)]
print(exp4)

# troca o 'a' por @
exp5 = [value.replace('a', '@').upper() for value in lista2]
print(exp5)

# retirando numeros impares da lista1
exp6 = [value for value in lista1 if value % 2 == 0]
print(exp6)

 # pegando elementos maires que 3
exp7 = [value for value in lista1 if value > 3]
print(exp7)

# pegando produtos que custam mais que 10 reais
exp8 = [value for value in produtos if value['preco'] > 10]
for value in exp8:
    print(value)
