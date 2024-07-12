'''
Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
Реализуйте еще один класс, который будет наследоваться от класса Calculato
r и перегрузите метод для вычисления суммы двух чисел,
 чтобы он делал конкатенацию двух строк.
'''


class Calculator:
    def add(self,x,y):
        return x+y


class StringCalculator(Calculator):

    def add(self, x, y):
        return str(x) + str(y)


c = StringCalculator()
print(c.add('sdsd', 'dfd'))

c = Calculator()
print(c.add(4,6))





