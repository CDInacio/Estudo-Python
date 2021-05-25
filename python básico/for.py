string = 'claudio vitor dantas'

for n in string:
    print(n)

print()
#---------------------------------------

# função range(start=0, stop, step=1)
for numero in range(10):
    print(numero)

print()
#---------------------------------------

for numero2 in range(5, 30, 5):
    print(numero2)

print()

#---------------------------------------

nome = 'claudio'
novo_nome = ''

for letra in nome:
    if letra == 'd':
        novo_nome += letra.upper()
    elif letra == 'i':
        novo_nome += letra.upper()
        break
    else:
        novo_nome += letra

print(novo_nome)

#---------------------------------------

lista = [
    [0, 'claudio'],
    [1, 'vitor'],
    [2, 'dantas'],
]

for key, value in lista:
    print(key, value)