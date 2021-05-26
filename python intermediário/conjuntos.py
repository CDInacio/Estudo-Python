# conjuntos so recebem valores e so suportam somente valores imutaveis
# conjuntos não possuem indices, diferente dos dicionarios, listas e tuplas,
# então não da pra acessar um valor em ESPECÍFICO diretamente do conjunto

# forma mais comum de criar um conjunto
conjunto = {
    1, 2, 3, 4
}

print(type(conjunto))

# outra forma de criar um conjutno(menos comum)
conjunto2 = set()

conjunto2.add('um')
conjunto2.add('dois')
conjunto2.add('tres')

print(conjunto2)

# removendo o valor de um conjunto
conjunto2.discard('tres')
print(conjunto2)

