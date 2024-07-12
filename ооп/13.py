"""
Реализуйте класс Dog. Придумайте, какие переменные будет принимать данный класс
и какие методы будут реализованы. Реализуйте в этом классе паттерн Singleton
"""


class Dog:

    bite = True
    legs = 4
    eyes = 2

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    def __del__(self):
        Dog.__instance = None

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)

d1 = Dog('it', 'black')
print(d1.name)
d1.name = 'alabay'
print(d1.name, d1.color)
d1.__setattr__('color','white')
print(d1.name, d1.color)
d2 = Dog('aff', 'gray')
print(d1.__dict__, '\n', d2.__dict__)
print(d1.eyes)