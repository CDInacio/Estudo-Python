#  iterável é um objeto que pode ser repetido . por exemplo, lista, string, tupla etc...

# iterável
lista = [1, 2, 3]
print(hasattr(lista, '__iter__'))
for value in lista:
    print(value)

# iterável
lista = 'string'
print(hasattr(lista, '__iter__'))

# não iterável
lista = 123
print(hasattr(lista, '__iter__'))
