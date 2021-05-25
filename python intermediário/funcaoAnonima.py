def mult(num1, num2):
    return num1 * num2

res = mult(2, 3)

# refazendo a  função acima com função anonima(função sem nome)
a = lambda numero1, numero2: numero1 * numero2
print(a(2, 2))

print()


# ordenando lista com funcao anonima
lista = [ 
    ['produto1', 13],
    ['produto2', 8],
    ['produto3', 5],
    ['produto4', 90],
]

lista.sort(key=lambda item: item[1])
print(lista)

# def ordernarPorPreco(item):
#     return item[1]

# lista.sort(key=ordernarPorPreco, reverse = True)
# print(lista)