"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobreNome: str


    def nome_completo(self):
        return f'{self.nome} {self.sobreNome}'


p1 = Pessoa('claudio', 'dantas')
p2 = Pessoa('natalia', 'paiva')

print(p1 == p2)

print(p1)
print(p1.nome_completo())
