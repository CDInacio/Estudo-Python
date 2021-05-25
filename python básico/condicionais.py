# IF, ELIF e ELSE

idade = int(input('Informe a sua idade: '))
acompanhantes  = int(input('Quantos acompanhantes? '))
idadeLimite = 18

if idade >= 18 and acompanhantes >= 1:
    print('Voce nao tem permissao para entrar, sinto muito')
elif idade < 18 and acompanhantes >= 1:
    print('Pode entrar')
else:
    print('Não pode entrar')
