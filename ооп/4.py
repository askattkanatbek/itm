'''Работаем с классом из 3 пункта. Реализуйте сеттеры и геттеры для цвета и марки транспортного средства.'''

class MeansOfTransport:
    
    def __init__(self, brand, color):
        if self.__check_value(brand) and self.__check_value(color):
            self.__brand = brand
            self.__color = color

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, str)
    
    def settter(self, brand, color):
        if self.__check_value(brand) and self.__check_value(color):
            self.__brand = brand
            self.__color = color
        else:
            raise ValueError('arguments must be string')
    
    def getter(self):
        return self.__brand, self.__color
    

my_car = MeansOfTransport('BMW', 'Black')
my_car.settter('Audi', 'White')
print(my_car.getter())
