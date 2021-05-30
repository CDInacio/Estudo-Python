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


p1 = Pessoa('claudio', 24)
print(p1.idade)
p1.nascimento()

print()

# pessoa criada a partir de um metodo de classe
p2 = Pessoa.por_ano_nascimento('vitor', 1945)
print(p2.idade)
p2.nascimento()
