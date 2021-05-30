from datetime import datetime

class Pessoa:
    # variável da classe
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        # variaveis de instancia
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return

        print(f'{self.nome} está comendo {alimento}!')
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
            return

        print(f'{self.nome} parou de comer!')
        self.comendo = False

    def falar(self):
        if self.falando:
            print(f'{self.nome} já está falando')
            return

        if self.comendo:
            print(f'{self.nome}, você não pode falar enquanto come!')
            return

        print(f'{self.nome} está falando!')
        self.falando = True

    def para_de_falar(self):
        if not self.falando:
            print(f'{self.nome} já parou de falar!')
            return

        print('Parando de falar!')
        self.falando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
