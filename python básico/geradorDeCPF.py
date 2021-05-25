cpf = '16899535001'
novo_cpf = cpf[:-2] 
reverso = 10
total = 0 

for index in range(19):
    if index > 8:
        index -= 9
    
    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        novo_cpf += str(digito)

if cpf == novo_cpf:
    print('cpf valido')
else:
    print('cpf invalido')