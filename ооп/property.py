from string import ascii_letters
class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        
        self.__fio = fio.split()
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('FIO must be string')
        f = fio.split()
        if len(f) !=3:
            raise TypeError('invalid')
        
        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) <1:
                raise TypeError('FIO must have at least 1 symbol')
            if len(s.strip(letters)) != 0:
                raise TypeError('FIO must have only letter and dash')
            
    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Age must be int and in range 14-120")
    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w<20:
            raise TypeError('Weight must be float and more than 20')
    @classmethod
    def verify_ps(cls,ps):
        if type(ps) != str:
            raise TypeError('Passport must be string')
        
        s = ps.split()
        if len(s) != 2 or len(s[0]) !=4 or len(s[1]) != 6:
            raise TypeError('invalid passport')
        
        for p in s:
            if not p.isdigit():
                raise TypeError('Seria and number of passport must be int')


    @property
    def fio(self):
        return self.__fio
    
    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight
    
    @property
    def passport(self):
        return self.__passport
    
    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps



p = Person('Балакиров Сергей Михайлович', 30, '1234 567890', 80.0)
p.old = 200
p.passport = '4567 123456'
p.weight = 70.0
print(p.old)
        