# List Comprehension é uma forma concisa de criar e manipular listas.

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

