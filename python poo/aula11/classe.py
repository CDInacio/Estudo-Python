class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # nome da classe
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nome} está falando na classe {self.nomeClasse}')


# cliente herda de pessoa
class Cliente(Pessoa):
    def comprar(self):
        print(f'O cliente {self.nome} está comprando')


# clientevip herda de cliente
# então clientevip é um cliente e uma pessoa
class ClienteVip(Cliente):
    # sobrepondo o construtor de pessoa
    def __init__(self, nome, idade, sobreNome):
        # Pessoa.__init__(self, nome, idade)
        super().__init__(nome, idade)
        self.sobreNome = sobreNome

    # sobrepondo um metodo, o metodo herdado de mesmo nome não será mais chamado
    def comprar(self):
        print('metodo sobreposto')

    # # sobrepondo o metodo falar
    def falar(self):
        print(f'o cliente vip {self.nome} {self.sobreNome} está falando')
        # formas de chamar um metodo
        # Pessoa.falar(self)
        # Cliente.falar(self)
        # super().falar()



