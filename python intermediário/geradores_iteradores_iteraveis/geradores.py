# Os geradores em Python são uma maneira simples de criar um objeto
# iterável sem a necessidade de construí-lo dentro de uma classe.

import sys
import time

# lista = list(range(1000))
# print(sys.getsizeof(lista))


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()
for value in g:
    print(value)

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))


def gera2():
    var = 'variavel 1'
    yield var
    var = 'variavel 2'
    yield var
    va1 = 'variavel 3'
    yield var


g2 = gera2()
for value in g2:
    print(value)

