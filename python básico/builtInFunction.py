numero1 = input('numero 1: ')
numero2 = input('numero 2: ')

# funções para verificar se a variável pode ser convertida em um numero inteiro: isnumeric, isdigit, isdecimal
if numero1.isdigit() and numero2.isdigit():
    numero1 = int(numero1)
    numero2 = int(numero2)

    print(numero1 + numero2)
else:
    print('nao foi possivel converter os numeros')


# try:
#     numero1 = int(numero1)
#     numero2 = int(numero2)

#     print(numero1 + numero2)
# except:
#     print('ERROR')
 