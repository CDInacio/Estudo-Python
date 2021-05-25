secreto = 'perfume'
digitados = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Voce precisar digitar uma letra!')
        continue

    digitados.append(letra)

    if letra in secreto:
        print(f'NICE! A letra digitada {letra} existe na palavra secreta!')
    else:
        print('Não foi dessa vez!')
        digitados.pop()
    
    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    
    if secreto_temp == secreto:
        print('VOCE GANHOU!')
        break
    else:
        print('VOCE PERDEU')