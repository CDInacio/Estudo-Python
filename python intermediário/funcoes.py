def saudacao(msg, nome):
    print(msg, nome)

saudacao('ola', 'claudio')
saudacao('fala comigo', 'natalia')

print()


# funcao com valores padroes
def saudacao2(msg ='boa noite', nome='fulano'):
    print(msg, nome)

saudacao2('boa noite', 'pun pun')
saudacao2()

print()


# geralmente não se utiliza print dentro da funcao
def divisao(n1, n2):
    return n1 / n2

resultado = divisao(40, 5)
print(resultado)

print()


def divisao2(num1, num2):   # se n2 for igual a 0 a funcao ira retornar none
    if num2 > 0:
        return num1 / num2

result = divisao2(30, 3)

if result:
    print(result)
else:
    print('operacao invalida')

print()



def divisao3(numero1, numero2):
    if numero2 == 0:
        return

    return numero1 / numero2

res = divisao3(10, 0)

if res:
    print(res)
else:
    print('operacao invalida')

print()


# retornando uma lista
def returnLista():
    return [1, 2, 3, 4, 5]

var = returnLista()
print(var, type(var))

print()


# funcao que retorna outra funcao sem executa-la
def func(var):
    print(var)

def dumb():
    return func

value = dumb()('primeira funcao aqui')

print()


# funcao com o numero de argumentos indefinido
def funcao(*args):
    for value in args:
        value *= 2
        print(value)

funcao(1, 2, 3, 4, 5)

print()


def funcao2(*args):
    print(args)

lista = [1, 2, 3, 4, 5]
funcao2(*lista)

print()


# **kwargs argumentos com palavras chave
def funcao3(*args, **kwargs):
    print(args)
    print(kwargs)

array = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]

funcao3(*array, *array2, nome = 'claudio', sobre_nome = 'dantas')

print()


def funcao4(*args, **kwargs):
    print(args)
    
    # é bom usar get quando não se tem certeza se determinada chave existe ou não
    marca = kwargs.get('marca')
    print(marca)

    preco = kwargs.get('preco')

    if preco is not None:
        print(preco)
    else:
        print('preco nao existe')

funcao4('deez', 'nuts', marca = 'nissan', modelo = 'gtr-r35')


    