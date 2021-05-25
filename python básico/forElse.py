# nomes = ['claudio', 'vitor', 'dantas']
# comeca_com_d = False

# for n in nomes:
#     if n.startswith('d'):
#         comeca_com_d = True

# if comeca_com_d:
#     print('existe uma palavra na lista que comeca com d')
# else:
#     print('nao existe uma palavra na lista que comeca com d')

nomes = ['claudio', 'vitor', 'antas']

for n in nomes:
    if n.lower().startswith('d'):
        print('existe uma palavra que comeca com d')
        break
else:
    print('nao existe uma palavra na lista que comeca com d')
