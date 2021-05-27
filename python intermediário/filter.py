
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

pessoas = [
    {'nome': 'Cláudio', 'idade': 14},
    {'nome': 'Sandro', 'idade': 28},
    {'nome': 'Natália', 'idade': 24},
    {'nome': 'Inácio', 'idade': 53},
    {'nome': 'Celso', 'idade': 9},
    {'nome': 'Mariana', 'idade': 23},
    {'nome': 'Dantas', 'idade': 10},
    {'nome': 'Hebert', 'idade': 21},
]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
####################################################

# a função FILTER retorna true ou false 

 # filtrando elementos maires que 5
nova_lista = filter(lambda value : value > 5, lista)
print(list(nova_lista))

# filtrando produtos que custam mais que 10 reais
novo_dicionario = filter(lambda value: value['preco'] > 10, produtos)
for value in novo_dicionario:
    print(value)

# desconto para produtos que custam mais que 50 reais
def desconto(produto):
    if produto['preco'] >= 50:
        produto['preco'] *= 0.5
    return produto

novo_dicionario2 = filter(desconto, produtos)
for value in novo_dicionario2:
    print(value)
print()

# filtrando produtos que custam mais que 20 reais
def mais_que_vinte(produto):
    if produto['preco'] > 20:
        return True

novo_dicionario3 = filter(mais_que_vinte, produtos)
for value in novo_dicionario3:
    print(value)
print()

# criando uma nova chave para produtos maiores que 25 reais
def ta_caro(produto):
    if produto['preco'] > 25:
        produto['ehCaro'] = True
    return True

novo_dicionario4 = filter(ta_caro, produtos)
for value in novo_dicionario4:
    print(value)
print()

# filtrando pessoa que são maiores de idade
def maior_de_idade(pessoas):
    if pessoas['idade'] >= 18:
        return True

novo_dicionario5 = filter(maior_de_idade, pessoas)
for value in novo_dicionario5:
    print(value)