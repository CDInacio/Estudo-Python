# um iterador vai te dar um valor de cada vez de um objeto iterável

lista = [1, 2, 3, 4]

# transformando a lista em um iterador
lista = iter(lista)
print(hasattr(lista, '__next__'))

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

