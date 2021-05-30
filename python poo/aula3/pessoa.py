# métodos estáticos
# Um método estático é um método que pode ser chamado sem a instancia da classe.

from random import randint


class Pessoa:
    # atributo de classe
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, nascimento):
        idade = cls.ano_atual - nascimento
        # retornando a propria classe
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(1, 1000)
        return rand


p1 = Pessoa('claudio', 24)
# o metodo pode ser chamado tanto pela instancia quanto pela classe
print(Pessoa.gera_id())
print(p1.gera_id())
