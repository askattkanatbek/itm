"""Создайте класс {{MeansOfTransport }}(для определения цвета и марки машины), 
принимающий 2 аргумента при инициализации (марка и цвет транспортного средства).
в этом классе реализуйте методы show_color(), выводящий на печать цвет транспортного средства и show_brand, 
для получения марки транспортного средства."""

class MeansOfTransport:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def show_color(self):
        return f'{self.color}'

    def show_brand(self):
        return f'{self.brand}'

my_car = MeansOfTransport('BMW', 'black')
print(my_car.show_brand())
print(my_car.show_color())
    

