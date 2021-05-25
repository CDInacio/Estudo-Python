# ESCOPO DE VARIÁVEIS

# variavel em escopo global
var = 'valor'   

def func():
    # essa variavel é deferente da variavel criada na linha 3
    # e ela so esta acessivel no escopo dessa funcao (func)
    var = 'outro valor'
    print(var)

func()

# o valor da variavel não foi alterado
print(var)

print()


# caso eu queria mudar o valor de uma variavel global dentro de uma funcao
# basta fazer o seguinte (n é uma boa pratica)
var2 = 'var global'

def func2():
    global var2 
    var2 = 'var local'
    print(var2)

func2()

print()


# uma forma de usar a variavel global numa funcao sem altera-la
def func3(arg = None):
    arg = arg.replace('v', 'c')
    return arg

result = func3(var)
print(result)

print()

