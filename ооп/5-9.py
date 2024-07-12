'''
Реализуйте два класса Car и Moped,
которые будут наследоваться от класса MeansOfTransport.
При инициализации они должны принимать новый аргументы(количество колес.
'''

'''
В классе {{Moped}}напишите статическую функцию, 
которая на вход будет принимать расстояние и максимальную скорость,
 а на выходе получать время, за которое проедет мопед это расстояние.
'''

'''
Попробуйте инициализировать несколько любых переменных в классе Car 
и сделайте одну переменную приватной, одну защищенной.
 Попробуйте получить к ним доступ. Какой результат?
'''

'''
В классе Car добавьте переменную класса car_drive = 4 
и реализуйте classmethod, который выводит на экран переменную car_drive
'''

'''
Реализуйте все возможные магические методы в классе Car.
'''
class MeansOfTransport:
    def __init__(self, name, year, side_of_steering_wheel):
        self.name = name
        self.year = year
        self.side_of_steering_wheel = side_of_steering_wheel


class Car(MeansOfTransport):
    car_drive = 4
    def __init__(self, name, year, side_of_steering_wheel):
        super().__init__(name, year, side_of_steering_wheel)
        self.__year = year
        self._side_of_steering_wheel = side_of_steering_wheel
        self.name = name

    def __len__(self):
        return len(self.name)

    def __abs__(self):
        return list(map(abs, self.__year, self._side_of_steering_wheel, self.name))

    def __str__(self):
        return f"Машина: {self.name} {self.year},Колеса: {self.car_drive}"

    def __repr__(self):
        return f'{self.__class__} :{self.name}'


    @classmethod
    def show(cls):
        print('количество колес', cls.car_drive)



class Moped(MeansOfTransport):

    def __init__(self, distance, velocity):
        self.distance = distance
        self.velocity = velocity

    @staticmethod
    def __timemoped__(distance, velocity):
        return distance / velocity

car = Car('BMW', 2018, 'left')
print(car.__repr__())


