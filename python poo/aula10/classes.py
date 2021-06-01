class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # nome da classe
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nome} está falando na classe {self.nomeClasse}')


# aluno herda de pessoa
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando')


# cliente herda de pessoa
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando')