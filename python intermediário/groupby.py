from itertools import groupby

alunos = [
    {'nome': 'claudio', 'nota': 'a'},
    {'nome': 'vitor', 'nota': 'a'},
    {'nome': 'dantas', 'nota': 'c'},
    {'nome': 'inacio', 'nota': 'b'},
    {'nome': 'sandro', 'nota': 'd'},
    {'nome': 'natalia', 'nota': 'b'}
]

# ordenando alunos pela nota
ordena = lambda item: item['nota']
alunos.sort(key = ordena)

alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
    print()