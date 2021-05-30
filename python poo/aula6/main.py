# se um atributo tiver um '_' antes do nome, recomenda-se que esse atributo não seja acessado
# _ protected(public) -> (não recomenda o acesso, apesar de ser possivel acessar)
# __ private -> (não acesse de jeito nenhum)

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    # se eu quiser permitir acesso à uma propriedade privada (nesse casso '__dados'), basta criar um getter
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados.items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

    def nova_chave(self, key, value):
        self.__dados['clientes'].update({key: value})


bd = BaseDeDados()
bd.inserir_cliente(1, 'claudio')
bd.inserir_cliente(2, 'sandro')
bd.apaga_cliente(2)
bd.lista_clientes()

# usando o getter
print(bd.dados)

# bd.nova_chave('aniversario', '31-07')
# print(bd._dados)
