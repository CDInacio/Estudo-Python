# Polimorfismo é um princípio que permite que classes derivadas de uma mesma superclasse tenham
# métodos iguais (de mesma assinatura) mas comportamentos diferentes.
# Mesma assinatura = Mesma quantidade e tipo de parametros

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg):
        pass


class B(A):
    def fala(self, msg):
        print(f'B falando: {msg}')


class C(A):
    def fala(self, msg):
        print(f'C falando: {msg}')


b = B()
b.fala('ola mundo')

c = C()
c.fala('ola mundo cruel')