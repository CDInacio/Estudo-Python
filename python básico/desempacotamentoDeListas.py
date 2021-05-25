nome = ['claudio', 'vitor', 'dantas']

n1, n2, n3 = nome
print(n2)

#------------------------------------------ 

nome2 = ['sandro', 'dantas', 'silva', 'inacio', 1, 2, 3, 4, 4, 100]

valor1, valor2, *outra_lista, ultimo_valor = nome2
print(valor1, valor2, outra_lista, ultimo_valor)

# *outra_lista, ultimo_valor = nome2
# print(outra_lista, ultimo_valor)
