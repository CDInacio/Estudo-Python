# dicionario é um tipo de estrutura de dados que suporta um par de chave/valor
# as chaves em um dicionário precisam ser ÚNICAS

# forma mais comum de criar um dicionario
dicionario = {
    'chave1': 'valor da chave'
}


# adicionando uma nova chave no dicionario
dicionario['nova_chave'] = 'valor da nova chave'
print(dicionario)


# mostrando o valor da chave
print(dicionario['nova_chave'])


# outra forma de criar um dicinoario (menos comum)
dicionario2 = dict(
    chave1='valor chave1',
    chave2='valor chave2'
)

dicionario2['chave3'] = 'valor chave3'

print(dicionario2)
print(dicionario2['chave2'])


# qualquer tipo de dado imutável pode ser usado como chave
dicionario3 = {
    'str': 'string',
    123: 'numeros',
    (1, 2, 3): 'tupla'
}

print(dicionario3[(1, 2, 3)])

# adicinoando uma nova chave no dicionario
dicionario3['chave4'] = 'valor da chave 4'  

# outra forma de adicionar uma nova chave no dicionario (menos usual)
dicionario3.update({    
    'chave5': 'valor da chave 5'
})

if dicionario3.get('chave4') is not None:
    print(dicionario3.get('chave4'))


# alterando o valor de uma chave no dicionario
dicionario3['str'] = 'nova string'  
print(dicionario3)

# excluindo uma chave do dicionario
del dicionario3['str']
print(dicionario3)

# verificando se existe uma chave no dicionario
if 123 in dicionario3:
    print(True)
else:
    print(False)

# verificando se existe um valor no dicionario
if 'tupla' in dicionario3.values():
    print(True)
else:
    print(False)

# verificando o numero de pares chave/valor no dicionario
print(len(dicionario3))

# iterando sobre um dicionario
for key, value in dicionario3.items():
    print(f'{key} = {value}')


# dicionario em um dicionario
cliente = {
    'cliente1': {
        'nome': 'Claudio',
        'sobreNome': 'Dantas'
    },
    'cliente2': {
        'nome': 'Natalia',
        'sobreNome': 'Paiva'
    },
    'cliente3': {
        'nome': 'Fulano',
        'sobreNome': 'Silva'
    },
    'cliente4': {
        'nome': 'Beltrano',
        'sobreNome': 'Oliveira'
    },
    'cliente5': {
        'nome': 'Ciclano',
        'sobreNome': 'Henrique'
    }
}

for cliente_key, cliente_Value in cliente.items():
    print(f'Exibindo {cliente_key}')
    for dados_Key, dados_Value in cliente_Value.items():
        print(f'{dados_Key} = {dados_Value}')
    

# copiando dicionario
# a forma abaixo não é uma boa pratica, porque se o valor de v for alterado, o valor de d1 também será, ja que ambas apontam para o mesmo endereõ de memória
d1 = {
    1: 'a',
    2: 'b',
    3: 'c'
}

v = d1

v[1] ='banana'

print(v)
print(d1)

# forma correta de copiar um dicionario
import copy

d2 = {
    1: 'a',
    2: 'b',
    3: 'c'
}

v2 = copy.deepcopy(d2)
v2[2] = 'banana'

print(v2)
print(d2)

#convertendo lista em dicionario
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d1 = dict(lista)
print(d1)

#convertendo lista com valures de tupla em dicionario
lista2 = [
    ('c1', 1),
    ('c2', 2),
    ('c3', 3),
]

d2 = dict(lista2)
print(d2)

"""
if 'nao_existe' in dicionario3:
    print(dicionario3['nao_existe'])
else:
    print('a chave nao existe')
"""


"""
if 'nao_existe' not in dicionario3:
    dicionario3['nao_existe'] = 'valor novo'
else:
    print(dicionario3['nao_existe'])

print(dicionario3)
"""
