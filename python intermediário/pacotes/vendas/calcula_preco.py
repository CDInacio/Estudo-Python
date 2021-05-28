def aumento(valor, porcentagem):
    res = valor + (valor * porcentagem / 100)
    return res


def reducao(valor, porcentagem):
    res = valor - (valor * porcentagem / 100)
    return res
