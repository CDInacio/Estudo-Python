from map import produtos, pessoas, lista

# pegando apenas os precos dos produtos
precos = map(lambda x: x['preco'], produtos)

for preco in precos:
    print(preco)

# aumentando o valor dos precos dos produtos
def aumento(produto):
    produto['preco'] = round(produto['preco'] * 1.05, 2)
    return produto

novo_produto = map(aumento, produtos)

for value in novo_produto:
    print(value)


# pegando apenas os nomes das pessoas do dicionario
nomes = map(lambda value: value['nome'], pessoas)

for value in nomes:
    print(value)
