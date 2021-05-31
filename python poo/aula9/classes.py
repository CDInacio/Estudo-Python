# composição: combinação de objetos, quando instanciamos objetos de
# uma classe dentro de outra, quando usamos objetos de uma classe
# dentro de outros objetos.

# forma mais forte de relacionamente entre classes
# se a classe principal for apagada, a secundaria tambèm será

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        # composição
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado