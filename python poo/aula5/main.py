class A:
    var = 123

    def mostrar(self):
        print(self.var - 10)


a1 = A()

# criando uma variavel de instancia
a1.var = 123
# alterando o valor da variavel de classe
A.var = 321

print(a1.var)
print(A.var)
print(a1.mostrar())
