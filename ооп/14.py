'''
Напишите класс, который принимает список людей
с интерфейсом добавления новых
и при итерации возвращал имена людей
'''


class People:
    def __init__(self, name):
        self.lst = []
        self.lst.append(name)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.lst):
            person = self.lst[self.index]
            self.index += 1
            return person
        else:
            raise StopIteration

    def __addperson__(self, name):
        self.lst.append(name)


collection = People('aslat')
collection.__addperson__('kamu')
collection.__addperson__('asa')
for person in collection:
    print(person)
