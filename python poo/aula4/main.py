class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # getter
    @property
    def nome(self):
        return self._nome

    # setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    # getter
    @property
    def preco(self):
        return self._preco

    # setter
    @preco.setter
    def preco(self, valor):
        # verificando o tipo da variavel
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('camisa', 100)
p1.desconto(80)
print(p1.preco)

p2 = Produto('short', 'R$100')
p2.desconto(8)
print(p1.preco)
