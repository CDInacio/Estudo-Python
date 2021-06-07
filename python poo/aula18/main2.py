"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python..
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""

from dataclasses import dataclass
from dataclasses import field



@dataclass(init=True, repr=True, eq=True, order=True, frozen=False)
class Pessoa:
    nome: str
    # omitindo o sobrenome no wrapper
    sobreNome: str = field(repr=False)

    # método chamado após o init
    def __post_init__(self):
        # verificando se o tipo nome está correto
        if not isinstance(self.nome, str):
            raise TypeError(f'Tipo inválido: {type(self.nome).__name__} != str em {self}')
        # self.nomeCompleto = '{self.nome} {self.sobreNome}'

    def nome_completo(self):
        return f'{self.nome} {self.sobreNome}'


# ordenando as pessoas
p1 = Pessoa('claudio', 'dantas')
p2 = Pessoa('natalia', 'paiva')
p3 = Pessoa('sandro', 'inacio')
p4 = Pessoa('claudio', 'inacio')
p5 = Pessoa('maria', 'aparecida')
p6 = Pessoa('ana', 'mares')

pessoas = [p1, p2, p3, p4, p5, p6]
# ordenando pelo nome
#print(sorted(pessoas))

# ordenando pelo sobrenome
print(sorted(pessoas, key=lambda pessoa: pessoa.sobreNome))


