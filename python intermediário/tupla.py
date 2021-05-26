# a diferença de tupla para lista é que as tuplas não podem ser alteradas

tupla = (1, 2, 3, 4, 'a', 'b', 'ola mundo')

print(tupla)
print(tupla[3])
print(tupla[-1])

for value in tupla:
    print(value)

# fatiando tuplas
nova_tupla = tupla[:4]
print(nova_tupla)

# as tuplas podem ser criadas sem os parenteses
tupla2 = 1, 2, 3, 4
print(tupla2, type(tupla2))

# concatenando tuplas
t1 = 1, 2, 3
t2 = 4, 5, 6, 'suco', 'biscoito'
t3 = t1 + t2
print(t3)

# desempacotando tuplas
n1, n2, n3, *resto_tupla = t3
print(n3)
print(resto_tupla)