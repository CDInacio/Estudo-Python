x = 0
# while x < 100:
#     print(x)
#     x += 1;
# print('ACABOU')

# while x < 20:
#     if x == 13:
#         break
#     print(x)
#     x += 1
# print('ACABOU')

# while x < 10:
#     y = 0
    
#     while y < 5:
#         print(f'x vale {x} e y vale {y}')
#         y += 1
    
#     x += 1

while True:
    numero1 = input('digite um numero: ')
    numero2 = input('digite outro numero: ')
    operador = input('digite um operador ')

    if not numero1.isnumeric() or not numero2.isnumeric():
        print('numero invalido')
        continue
    
    numero1 = int(numero1)
    numero2 = int(numero2)

    if operador == '+':
        print(numero1 + numero2)
    elif operador == '-':
        print(numero1 - numero2)
    elif operador == '/':
        print(numero1 / numero2)
    elif operador == '*':
        print(numero1 * numero2)
    else:
        print('operador invalido')
