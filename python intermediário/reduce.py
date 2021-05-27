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

from functools import reduce

# reduce faz acumulação de valores

lista = [1, 2, 3, 4, 5]

soma_lista = reduce(lambda value, item: item + value, lista, 0)
print(soma_lista)

# soma total dos precos dos produtos
soma_precos = reduce(lambda value, item: item['preco'] + value, produtos, 0)
print(soma_precos)


# geral = 0
# for value in produtos:
#     geral += value['preco']
# print(geral)