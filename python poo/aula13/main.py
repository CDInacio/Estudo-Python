# As classes abstratas são as que não permitem realizar
# qualquer tipo de instância. São classes feitas especialmente
# para serem modelos para suas classes derivadas. As classes
# derivadas, via de regra, deverão sobrescrever os métodos para
# realizar a implementação dos mesmos. As classes derivadas das
# classes abstratas são conhecidas como classes concretas.

from contaPoupanca import ContaPoupanca
from contaCorrente import ContaCorrente


cp = ContaPoupanca(111, 222, 0)
cp.depositar(100)
cp.sacar(20)
cp.sacar(81)

cc = ContaCorrente(333, 444, 0, 500)
cc.sacar(300)
