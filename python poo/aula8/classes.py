# Uma Agregação também é uma composição, mas com uma característica diferente:
# os objetos existem independemente um do outro.

# a classe CarrinhoDeCompras pode existir sozinha mas ela precisa da classe Produto
# para executar suas ações

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(f'{produto.nome} = R$ {produto.valor}')

    def soma_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.valor
        return round(soma, 2)


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor