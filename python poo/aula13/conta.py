from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        # checando se o valor não é inteiro ou ponto flutuante
        if not isinstance(valor, (int, float)):
            raise ValueError('O saldo precisa ser numerico')

        self._saldo += valor

    def detalhes(self):
        print()
        print(f'Agencia: {self.agencia}')
        print(f'Conta: {self.conta}')
        print(f'Saldo: {self.saldo}')
        print()

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('O valor do deposito precisa ser numerico')
        self.saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass

