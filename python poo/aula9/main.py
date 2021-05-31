# composição: combinação de objetos, quando instanciamos objetos de
# uma classe dentro de outra, quando usamos objetos de uma classe
# dentro de outros objetos.

# forma mais forte de relacionamente entre classes
# se a classe principal for apagada, a secundaria tambèm será

from classes import Cliente

cliente1 = Cliente('Claudio', 24)
cliente1.insere_endereco('Salvador', 'BA')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Natalia', 24)
cliente2.insere_endereco('João Monlevade', 'MG')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Sandro', 27)
cliente3.insere_endereco('Serrinha', 'BA')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
