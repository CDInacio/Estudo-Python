# sistema de perguntas e respostas

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto eh 2 + 2? ',
        'respostas': {
            'a': '1',
            'b': '3',
            'c': '4',
            'D': '2'
        },
        'resposta_certa': 'c'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto eh 5 * 5? ',
        'respostas': {
            'a': '10',
            'b': '20',
            'c': '24',
            'D': '25'
        },
        'resposta_certa': 'd'
    },
}

respostas_certas = 0
for pergunta_key, pergunta_value in perguntas.items():
    print(f'{pergunta_key}: {pergunta_value["pergunta"]}')

    print('Respostas')
    for resposta_key, resposta_value in pergunta_value['respostas'].items():
        print(f'[{resposta_key}]: {resposta_value}')

    resposta_usuario = input('Sua resposta: ')
    if resposta_usuario == pergunta_value['resposta_certa']:
        print('Nice, resposta correta!')
        respostas_certas += 1
    else:
        print('Aff, não foi dessa vez!')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Sua porcentagem de acerto foi de {porcentagem_acerto:.0f} %')
