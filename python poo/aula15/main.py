class TaErradoError(Exception):
    pass


def testa():
    raise TaErradoError('errado')


try:
    testa()
except TaErradoError as err:
    print(f'Erro: {err}')