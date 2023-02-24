import math


class QuadraticEq:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def show_eq(self):
        print(str(self.a) + 'x^2' + ('+' if self.b >= 0 else '') + str(self.b) + 'x' + ('+' if self.c >= 0 else '')
              + str(self.c))
        print('roots are:', self.find_roots()[0], self.find_roots()[1])

    def find_d(self):
        return self.b**2 - 4*self.a * self.c

    def find_roots(self):
        if self.find_d() < 0:
            x1 = round(-self.b / (2*self.a), 2) + round(math.sqrt(abs(self.find_d())) / (2*self.a), 5) * 1j
            x2 = round(-self.b / (2 * self.a), 2) - round(math.sqrt(abs(self.find_d())) / (2 * self.a), 5) * 1j
        elif self.find_d() == 0:
            x1 = x2 = round(-self.b / (2*self.a), 2)
        else:
            x1 = round(round(-self.b / (2*self.a), 2) + round(math.sqrt(self.find_d()) / (2*self.a), 5), 5)
            x2 = round(round(-self.b / (2 * self.a), 2) - round(math.sqrt(self.find_d()) / (2 * self.a), 5), 5)

        return [x1, x2]