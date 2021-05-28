# from functools import reduce


# def multiplica(lista):
#     res = 1
#     res = reduce(lambda value, item: item * value, lista, 1)
#     return res

# def dobra(lista):
#     return map(lambda value: value * 2, lista)

# lista = [1, 2, 3, 4, 5]

# nova = dobra_lista(lista)

# for value in nova:
#     print(value)


def dobra(lista):
    return [value * 2 for value in lista]


def multiplica(lista2):
    res = 1
    for value in lista2:
        res *= value
    return res


if __name__ == '__main__':
    lista3 = [1, 2, 3, 4, 5]
    print(multiplica(lista3))
    print(dobra(lista3))
