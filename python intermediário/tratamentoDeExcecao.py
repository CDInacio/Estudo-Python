try:
    a = []
    print(a[0])
# pega um erro especifico
except NameError as err:
    print('erro do desenvolvedor')
# pega mais de um erro na mesma linha de codigo
except (IndexError, KeyError) as err:
    print('erro de indice ou chave')
# pega qualquer tipo de erro
except Exception as err:
    print('ocorreu um erro inesperado')
# bloco else sera executado sempre que não houver erros
else:
    print('codigo executado com sucesso')
# o bloco finaly sempre sera executado, com ou sem erros no codigo
finally:
    print('finalmente')

print('o codigo continua...')
    
