# No python, o comportamento de operadores é definido por métodos especiais.
# Vamos alterar o comportamento de operadores com classes definidas pelo usuario.


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    # soma
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    # menor que
    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    # maior que
    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False


r1 = Retangulo(10, 5)
r2 = Retangulo(20, 10)
r3 = r1 + r2
print(r3)
print(r3 < r1)
print(r2 > r1)